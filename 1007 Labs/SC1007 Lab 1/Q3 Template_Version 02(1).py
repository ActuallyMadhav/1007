class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
    def __init__(self):
       self.head = None

    def insert(self, data, index):
       new_node = Node(data)
       if self.head is None or index == 0:
           new_node.next = self.head
           self.head = new_node
           return True
   
       current = self.head
       count = 0
   
       while current and count < index - 1:
           current = current.next
           count += 1
   
       if not current:
           print("Index out of range")
           return False
       
       new_node.next = current.next
       current.next = new_node
       return True

    def printList(self):
       current = self.head
       while current:
           print(current.data, end=" ")
           current = current.next
       print()

    def deleteList(self):
       current = self.head
       while current:
           temp = current.next
           current.next = None
           current = temp
       self.head = None

    def getSize(self):
       cur = self.head
       size = 0
       while cur:
            size += 1
            cur = cur.next
       return size 
#####################################################################
    def split(self):
        #write your code here #
        even_list = LinkedList()
        odd_list = LinkedList()

        cur = self.head
        even_tail = None
        odd_tail = None
        index = 0

        while cur:
            new_node = Node(cur.data)

            if index % 2 != 0:
                if odd_list.head is None:
                    odd_list.head = new_node
                    odd_tail = new_node
                else:
                    odd_tail.next = new_node
                    odd_tail = odd_tail.next
            else:
                if even_list.head is None:
                    even_list.head = new_node
                    even_tail = new_node
                else:
                    even_tail.next = new_node
                    even_tail = even_tail.next
            
            cur = cur.next
            index += 1
        return even_list, odd_list

#####################################################################
if __name__ == "__main__":
   linked_list = LinkedList()
   index = 0
   
   print("Enter one number per line (press Enter after each number).")
   print("Enter any non-digit character to finish input:")
   try:
       while True:
           item = int(input())
           if linked_list.insert(item, index):
               print(f"Successfully inserted {item} at index {index}")
               index += 1
           else:
               print(f"Failed to insert {item}")
   except ValueError:
       pass

   print("\nBefore split() is called:")
   print("The original list:", end=" ")
   linked_list.printList()
   
   even_list, odd_list = linked_list.split()
   
   print("\nAfter split() was called:")
   print("The original list:", end=" ")
   linked_list.printList()
   
   print("The even list:", end=" ")
   even_list.printList()
   
   print("The odd list:", end=" ")
   odd_list.printList()
   
   linked_list.deleteList()
   even_list.deleteList()
   odd_list.deleteList()