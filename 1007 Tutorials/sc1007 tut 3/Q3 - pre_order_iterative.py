class Bst_node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Stack_node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

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

def push(stack, node):
    temp = Stack_node(node)

    if stack.top is None:
        stack.top = temp
        temp.next = None
    else:
        temp.next = stack.top
        stack.top = temp

def pop(s):
    if s.top is None:
        return None

    temp = s.top.next
    ptr = s.top.data
    s.top = temp
    return ptr

def peek(s):
    if s.top is None:
        return None
    return s.top.data

def isEmpty(s):
    return s.top is None

def removeAll(node_ref):
    if node_ref[0] is not None:
        removeAll([node_ref[0].left])
        removeAll([node_ref[0].right])
        node_ref[0] = None

def pre_order_iterative(root):
    raise NotImplementedError

def main():
    root = [None]  # Using list to simulate pointer reference

    print("1: Insert an integer into the binary search tree;")
    print("2: Print the pre-order traversal of the binary search tree;")
    print("0: Quit;")

    while True:
        try:
            c = int(input("Please input your choice(1/2/0): "))

            if c == 1:
                i = int(input("Input an integer that you want to insert into the Binary Search Tree: "))
                insert_bst_node(root, i)

            elif c == 2:
                print("The resulting pre-order traversal of the binary search tree is: ", end="")
                pre_order_iterative(root[0])
                print()

            elif c == 0:
                removeAll(root)
                break

            else:
                print("Choice unknown;")

        except ValueError:
            print("Invalid input")
            continue


if __name__ == "__main__":
    main()