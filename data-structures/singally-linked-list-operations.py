"""Below python is for linked list operations using classes in python"""

#define the strucute of the linked list and initialize the object
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
#defint the linked and its functions
class Linked_list: 
    def __init__(self):
        self.head = None #initialize the head pointer

    def insert_at_head(self, data):
        #create a new node with the data value using the object of Node
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for _ in range(position - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    def display_list(self):
        list_elements = []
        temp = self.head
        while temp:
            list_elements.append(str(temp.data))
            temp = temp.next
        return ' -> '.join(list_elements)
    
list1 = Linked_list()
list1.insert_at_head(2)
list1.insert_at_head(1)
list1.insert_at_position(3,2)
print(list1.display_list())