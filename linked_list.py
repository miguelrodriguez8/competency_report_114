class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None # Equivalent to Null

#Node class
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None




if __name__=='__main__':
    # start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    """
    3 Nodes have been created.
    We have references to these blocks as head, second, and third.

    """
    llist.head.next = second # link first node with second
    second.next = third
    """
     Now next of first Node refers to these 3 blocks
    """
    my_node = llist.head
    while True:
        if my_node:
            print(my_node.data)
            my_node = my_node.next
        else:
            break
