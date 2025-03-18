class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        cur = self.head
        
        while cur:
            print(cur.data, end = ' -> ' if cur.next else '\n')
            cur = cur.next
    
    def insert_at_end(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return self.head
        
        cur = self.head
        prev = None

        while cur.next:
            cur = cur.next
        cur.next = newNode
        return self.head
    
    def delete(self, value):
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
            return 
        
    def reverse(self):
        cur = self.head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev
        return self.head


ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()  # Expected: 10 -> 20 -> 30
ll.reverse()
ll.display()

# ll.delete(20)
# ll.display()  # Expected: 10 -> 30

# ll.delete(10)
# ll.display()  # Expected: 30

