class Bt_node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Stack_node:
    def __init__(self, btnode):
        self.btnode = btnode
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

def create_bt_node(item):
    return Bt_node(item)

def push(stack, node):
    temp = Stack_node(node)
    if stack.top is None:
        stack.top = temp
        temp.next = None
    else:
        temp.next = stack.top
        stack.top = temp

def pop(stack):
    if stack.top is None:
        return None

    temp = stack.top.next
    ptr = stack.top.btnode
    stack.top = temp
    return ptr

def print_tree(node):
    if node is None:
        return
    print_tree(node.left)
    print(node.item, end=" ")
    print_tree(node.right)

def create_tree():
    stack = Stack()
    root = None

    print("Input an integer that you want to add to the binary tree. Any Alpha value will be treated as NULL.")
    try:
        item = input("Enter an integer value for the root: ")
        root = create_bt_node(int(item))
        push(stack, root)
    except ValueError:
        return None

    while True:
        temp = pop(stack)
        if temp is None:
            break

        try:
            item = input(f"Enter an integer value for the Left child of {temp.item}: ")
            temp.left = create_bt_node(int(item))
        except ValueError:
            temp.left = None

        try:
            item = input(f"Enter an integer value for the Right child of {temp.item}: ")
            temp.right = create_bt_node(int(item))
        except ValueError:
            temp.right = None

        if temp.right is not None:
            push(stack, temp.right)
        if temp.left is not None:
            push(stack, temp.left)

    return root

def remove_all(node):
    if node is not None:
        remove_all(node.left)
        remove_all(node.right)
        node.left = None
        node.right = None

def max_depth(node):
    if node is None:
        return -1
    else:
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

def main():
    root = None

    print("1: Create a binary tree.")
    print("2: Find the maximum depth of the binary tree.")
    print("0: Quit;")

    while True:
        try:
            c = int(input("\nPlease input your choice(1/2/0): "))

            if c == 1:
                root = None  # Clear existing tree
                root = create_tree()
                print("The resulting binary tree is: ", end="")
                print_tree(root)
                print()

            elif c == 2:
                depth = max_depth(root)
                print(f"The maximum depth of the binary tree is: {depth}")
                root = None

            elif c == 0:
                if root:
                    remove_all(root)
                break

            else:
                print("Choice unknown;")

        except ValueError:
            continue

if __name__ == "__main__":
    main()