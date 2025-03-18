class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None

    # def insert_at_end(self, value):
    #     new_node = Node(value)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next
    #     temp.next = new_node

    # def delete(self, value):
    #     temp = self.head
    #     if temp and temp.data == value:
    #         self.head = temp.next
    #         return
    #     prev = None
    #     while temp and temp.data != value:
    #         prev = temp
    #         temp = temp.next
    #         if temp:
    #             prev.next = temp.next

    def delete_at_beginning(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        del temp
        return self.head
    
    def delete_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            del self.head
            return None
        
        cur = self.head

        while cur.next.next:
            prev = cur
            cur = cur.next
        cur.next = None
        return self.head
        
    def delete_at_index(self, index):
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        cur = self.head
        prev = None
        count = 0

        while cur and count < index:
            prev = cur
            cur = cur.next
            count += 1

        if cur is None:
            print("Index is out of range")
            return False

        prev.next = cur.next
        return True


            

    def search(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                return print("element found")
            cur = cur.next

        return print("element not found")

    def printList(self):
        cur = self.head
        prev = None

        while cur:
            print(cur.data, end=' -> ' if cur.next else '\n')
            prev = cur
            cur = cur.next

    def getLength(self):
        counter = 0
        cur = self.head
        prev = None

        while cur:
            counter += 1
            prev = cur
            cur = cur.next

        return counter
    
    def insert_at_beginning(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        return temp
    
    def insert_at_end(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return self.head
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        return self.head
    
    def insert_at_index(self, value, index):
        newNode = Node(value)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return self.head
        
        count = 0
        cur = self.head
        prev = None

        if index > self.getLength():
            self.insert_at_end(value)
            return self.head

        while cur and count < index:
            prev = cur
            cur = cur.next
            count += 1
        
        if prev:
            prev.next = newNode
        newNode.next = cur

        return self.head
    
    def get_at_index(self, index):
        if index < 0 or index > self.getLength():
            return -1
        
        count = 0
        cur = self.head

        while cur and count < index:
            cur = cur.next
            count += 1
        if cur is None:
            return -1
        
        return cur.data
        

    # def display(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.data, end=" -> " if temp.next else '\n')
    #         temp = temp.next

    # def reverseLinkedList(self):
    #     prev = None
    #     cur = self.head
        
    #     while cur:
    #         nextNode = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = nextNode
    #     self.head = prev

    def reverseLinkedList(self):
        if self.head is None:
            return None
        prev = None
        cur = self.head

        arr = []

        while cur:
            arr.append(cur.data)
            prev = cur
            cur = cur.next
        
        arr = arr[::-1]

        cur = self.head
        for i in range(len(arr)):
            cur.data = arr[i]
            cur = cur.next
        return self.head

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.printList()  # Expected: 10 -> 20 -> 30
ll.reverseLinkedList()
 #ll.printList()  
# ll.search(40)  
# print(ll.getLength())  
# ll.insert_at_beginning(69)
# ll.printList()
# ll.insert_at_index(50, 7)
# ll.printList()
# print(ll.get_at_index(3))
# ll.delete_at_beginning()
# ll.printList()
#ll.insert_at_end(40)
ll.printList()
#ll.delete_at_end()
ll.delete_at_index(2)
ll.printList()
