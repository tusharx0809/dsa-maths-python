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
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def display_list(self):
        list_elements = []
        temp = self.head
        while temp:
            list_elements.append(str(temp.data))
            temp = temp.next
        return ' -> '.join(list_elements)
    
list1 = Linked_list()
list1.insert_at_head(1)
list1.insert_at_head(2)
print(list1.display_list())