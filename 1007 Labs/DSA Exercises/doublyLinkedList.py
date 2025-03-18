class Node:
    def __init__ (self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return self.head
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur

        return self.head

    def insert_at_beginning(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return self.head
        
        cur = self.head
        cur.prev = newNode
        newNode.next = cur
        self.head = newNode
        return self.head
    
    def delete_at_beginning(self):
        if self.head is None:
            return
        
        cur = self.head
        self.head = cur.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        
        if cur.prev:
            cur.prev.next = None
        else:
            self.head = None

    def delete_value(self, value):
            if self.head is None:
                return None
            cur = self.head
            if cur.data == value:
                self.delete_at_beginning()
                return
            
            while cur and cur.data != value:
                cur = cur.next
            
            if cur:
                if cur.next:
                    cur.next.prev = cur.prev
                if cur.prev:
                    cur.prev.next = cur.next

    def delete_at_index(self, idx):
        if self.head is None:
            return self.head
        
        cur = self.head

        if idx == 0:
            self.head = cur.next
            if self.head:  # If there is a node after the head
                self.head.prev = None  # Update the new head's prev pointer
            return self.head

        for i in range(idx):
            if cur is None:
                return self.head
            cur = cur.next

        if cur is None:
            return self.head
        
        if cur.next:
            cur.next.prev = cur.prev

        if cur.prev:
            cur.prev.next = cur.next
        
        return self.head

    def display(self):
        cur = self.head

        while cur:
            print(cur.data, end = ' <-> ' if cur.next else '\n')
            cur = cur.next

    def forward_traversal(self):
        if self.head is None:
            return None
        cur = self.head
        while cur is not None:
            print(cur.data, end=' <-> ' if cur.next else '\n')
            cur = cur.next

    def backward_traversal(self):
        if self.head is None:
            return 
        cur = self.head
        while cur.next:
            cur = cur.next
        
        while cur:
            print(cur.data, end=' <-> ' if cur.prev else '\n')
            cur = cur.prev

    def getLength(self):
        counter = 0
        cur = self.head
        while cur is not None:
            cur = cur.next
            counter += 1
        return counter

    def reverseDoublyLinkedList(self):
        cur = self.head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            cur.prev = temp
            prev = cur
            cur = temp
        self.head = prev
        return self.head


# Testing the DLL
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.forward_traversal()  # Expected: 10 <-> 20 <-> 30
#dll.insert_at_beginning(5)
#dll.forward_traversal()  # Expected: 5 <-> 10 <-> 20 <-> 30
#dll.backward_traversal()
dll.reverseDoublyLinkedList()
dll.display()
print(dll.getLength())

#dll.delete_at_beginning()
#dll.display()  # Expected: 20 <-> 30 <-> 40

# Delete from the end
#dll.delete_at_end()
#dll.display()  # Expected: 20 <-> 30

# Delete specific value
#dll.delete_value(20)
#dll.display() 

# Delete node at index 0 (using delete_at_beginning internally)
# dll.delete_at_index(0)
# dll.display()  # Expected: 20 <-> 30 <-> 40

# # Delete node at index 1 (value 30)
# dll.delete_at_index(1)
# dll.display()  # Expected: 20 <-> 40