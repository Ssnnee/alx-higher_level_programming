#!/usr/bin/python3

#!/usr/bin/python3

"""
This module contains two classes
for  defining a 'Node' class for a singly-linked list
"""


class Node:
    """This class defines a node of a singly linked list."""

    def __init__(self, data, next_node=None) -> None:
        """Initializes a new Node instance."""

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrieves data"""

        return self.__data

    @data.setter
    def data(self, value):
        """Allows data to be set"""

        if not type(value) is int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Allows next_node to be set"""

        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list"""

    def __init__(self) -> None:
        """Initializes a new Singly Linked List instance."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted
        position in the list (increasing order)
        """

        newNode = Node(value)
        if self.__head is None:
            newNode = self.__head
        elif value < self.__head.data:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            # newNode = self.__head
            n = self.__head
            while n.next_node is not None and n.next_node.data < value:
                n = n.next_node
            newNode.next_node = n.next_node
            n.next_node = newNode

    def __str__(self):
        """The to string method"""
        node = self.__head
        nodes_list = []
        while node is not None:
            nodes_list.append(str(node.data))
            node = node.next_node
        return "".join(nodes_list)
