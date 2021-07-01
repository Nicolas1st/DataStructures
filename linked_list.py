class Node:


    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    



class SinglyLinkedList:


    def __init__(self, array):
        
        self.first_node = Node(array[0])

        previous_node = self.first_node
        for value in array[1:]:
            new_node = Node(value)
            previous_node.next_node = new_node
            previous_node = new_node 

        self.last_node = previous_node


    def delete(self, node_index):

        """Removes an element from a singly linked list
        Input: index of the node to be removed
        Return: True if removed, False if there is no node with the index given"""

        if node_index < 0 and type(node_index) is int:
            print("Index is smaller than 0")
            return False

        if self.first_node is None:
            print("The list is empty")
            return False
        
        if node_index == 0:
            try:
                self.first_node = self.first_node.next_node
            except:
                self.first_node = None
            return True

        previous_node = self.first_node
        index = 1

        while True:

            current_node = previous_node.next_node
            
            if  current_node is None:
                if index == node_index:
                    return True
                print(f"The element at index {node_index} does not exist")
                print(f"The list length is equal to {index}")
                return False

            if index == node_index:
                if current_node.next_node is None:
                    previous_node.next_node = None
                else:
                    previous_node.next_node = current_node.next_node
                return True

            previous_node = current_node
            index += 1


    def insert(self, value, node_index):

        if node_index < 0:
            print(f"Can not insert the {value} at index {node_index}")
            return False

        if node_index == 0:
            self.first_node = Node(value, self.first_node)
            return True

        previous_node = self.first_node 
        index = 1 

        while previous_node is not None:

            node = previous_node.next_node 

            if node_index == index:
                next_node = previous_node.next_node
                previous_node.next_node = Node(value, next_node)
                return True

            previous_node = node
            index += 1

        return False


    def read(self, node_index):

        current_node = self.first_node
        index = 0

        while True:

            if node_index == index:
                return current_node.value

            current_node = current_node.next_node       

            if current_node is None:
                print(f"The node at index {node_index} does not exist")
                print(f"The lenght of the list is equal to {index+1}")
                return None
            
            index += 1


    def __repr__(self):

        values = []
        node = self.first_node

        while node is not None:
            values.append(node.value)
            node = node.next_node

        return str(values)



if __name__ == "__main__":

    array = list(range(10))
    linked_list  = SinglyLinkedList(array)
    print(linked_list)

    linked_list.delete(5)
    print(linked_list)

    print(linked_list.read(5))

    linked_list.insert(11, 1)
    linked_list.insert(12, 0)
    linked_list.insert("last element", 11)
    print(linked_list)
