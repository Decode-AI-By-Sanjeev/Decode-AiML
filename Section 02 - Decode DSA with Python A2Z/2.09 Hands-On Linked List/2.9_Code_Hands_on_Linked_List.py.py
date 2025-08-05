# -*- coding: utf-8 -*-
"""2.9_code.ipynb

# Linked List Implementation

We need to implement a menu-driven Linked List program in Python using the while loop.

We will create a singly linked list that supports:
1. Insert node
2. Delete node
3. Search node
4. Display list
5. Exit

### 1. Node Class
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""### 2. Linked List Class"""

# This class will manage the nodes and operations.

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at a specific index
    def insert_at_index(self, index, data):
        new_node = Node(data)

        # Insert at the beginning (index 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"Node {data} inserted at index {index}.")
            return

        temp = self.head
        count = 0

        # Traverse to the position before the index
        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Index out of range!")
            return

        new_node.next = temp.next
        temp.next = new_node
        print(f"Node {data} inserted at index {index}.")

    # 2. Delete node at a specific index
    def delete_at_index(self, index):
        # If list is empty
        if self.head is None:
            print("Linked List is empty!")
            return

        temp = self.head

        # If head needs to be deleted
        if index == 0:
            self.head = temp.next
            print(f"Node at index {index} deleted successfully!")
            return

        count = 0
        prev = None

        # Traverse to the position
        while temp is not None and count < index:
            prev = temp
            temp = temp.next
            count += 1

        # If index is out of range
        if temp is None:
            print("Index out of range!")
            return

        prev.next = temp.next
        print(f"Node at index {index} deleted successfully!")

    # 3. Search a node by value
    def search(self, key):
        temp = self.head
        position = 0
        while temp:
            if temp.data == key:
                print(f"Node with value {key} found at position {position}!")
                return
            temp = temp.next
            position += 1
        print(f"Node with value {key} not found!")

    # 4. Display linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Linked List Menu program


ll = LinkedList()

while True:
    option = int(input("""
              Enter an Operation you want to Execute on Linked List.\n
              1. Insert a node at Index i\n
              2. Delete a node at Index i\n
              3. Search a node in Linked List\n
              4. Display Linked List\n
              5. Exit\n
              """))

    if option == 1:
        idx = int(input("Enter index to insert: "))
        data = int(input("Enter value to insert: "))
        ll.insert_at_index(idx, data)

    elif option == 2:
        idx = int(input("Enter index to delete: "))
        ll.delete_at_index(idx)

    elif option == 3:
        data = int(input("Enter value to search: "))
        ll.search(data)

    elif option == 4:
        ll.display()

    elif option == 5:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Option! Please try again.")

