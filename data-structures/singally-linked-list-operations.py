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

        for _ in range(position - 2): #traverse till the node which is one less than positions
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
    
    def insert_from_end(self, data, position):
        new_node = Node(data)
        total_nodes = 0
        temp = self.head 

        while temp:
            temp = temp.next
            total_nodes += 1
        temp2 = self.head
        for _ in range(total_nodes - position): #subtract position from total nodes to insert from end
            temp2 = temp2.next
        new_node.next = temp2.next
        temp2.next = new_node
    def delete_node_from_position(self, position):
        if position == 1:
            self.head = self.head.next
            return
        
        temp = self.head
        prev = None
        for _ in range(position - 1):
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def display_list(self):
        list_elements = []
        temp = self.head
        while temp:
            list_elements.append(str(temp.data))
            temp = temp.next
        print(' -> '.join(list_elements)+" -> NULL")
    
list1 = Linked_list()
list1.insert_at_head(3)
list1.insert_at_head(2)
list1.insert_at_head(1)
#till now the list will print as 1 -> 2 -> 3 -> NULL
list1.display_list()
list1.insert_at_position(55,2)
#at second position, 55 will be inserted and list will look like 1 -> 55 -> 2 -> 3 -> NULL
list1.display_list()
#below function will delte the 3rd node which is
list1.delete_node_from_position(3)
#now the list is 1 -> 55 -> 3 -> NULL
list1.display_list()