class Bst_node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Queue_node:
    def __init__(self, data):
        self.data = data
        self.next_ptr = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

def insert_bst_node(node_ref, value):
    if node_ref[0] is None:
        node_ref[0] = Bst_node(value)
    else:
        if value < node_ref[0].item:
            if node_ref[0].left is None:
                node_ref[0].left = Bst_node(value)
            else:
                insert_bst_node([node_ref[0].left], value)
        elif value > node_ref[0].item:
            if node_ref[0].right is None:
                node_ref[0].right = Bst_node(value)
            else:
                insert_bst_node([node_ref[0].right], value)

def enqueue(queue, node):
    new_node = Queue_node(node)

    if is_empty(queue.head):
        queue.head = new_node
    else:
        queue.tail.next_ptr = new_node

    queue.tail = new_node

def dequeue(queue):
    if queue.head is not None:
        node = queue.head.data
        queue.head = queue.head.next_ptr
        if queue.head is None:  # If the queue becomes empty
            queue.tail = None
        return node
    return None

def is_empty(head):
    return head is None

def remove_all(node_ref):
    if node_ref[0] is not None:
        remove_all([node_ref[0].left])
        remove_all([node_ref[0].right])
        del node_ref[0]

def level_order_traversal(root):
    queue = Queue()
    temp = root

    if temp is not None:
        enqueue(queue, temp)
        while not is_empty(queue.head):
            temp = dequeue(queue)
            print(temp.item, end=' ')
            if temp.left is not None:
                enqueue(queue, temp.left)
            if temp.right is not None:
                enqueue(queue, temp.right)

# Main function to run the program.
if __name__ == "__main__":
    c = 1
    root = [None]  # Use a list to allow modification of the root reference

    print("1: Insert an integer into the binary search tree;")
    print("2: Print the level-order traversal of the binary search tree;")
    print("0: Quit;")

    while c != 0:
        c = int(input("Please input your choice(1/2/0): "))

        if c == 1:
            i = int(input("Input an integer that you want to insert into the Binary Search Tree: "))
            insert_bst_node(root, i)

        elif c == 2:
            print("The resulting level-order traversal of the binary search tree is: ", end="")
            level_order_traversal(root[0])  # Pass the actual root node
            print()

        elif c == 0:
            remove_all(root)

        else:
            print("Choice unknown;")