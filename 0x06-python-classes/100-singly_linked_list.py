#!/usr/bin/python3
"""This module holds the code for Node and SinglyLinkedList classes"""


class Node:
    """Node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes object to contain data and next_node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data attribute"""

        return self.__data

    @data.setter
    def data(self, value):
        """setter for data attribute"""

        if type(value) != int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """getter property for attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node attribute"""

        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A singly linked list made up of Node objects"""

    def __init__(self):
        """ Instantiates an empty list """

        self.__head = None

    def __str__(self):
        """Returns a string made up of the integer data in the nodes that
        make up the SinglyLinkedList"""

        start = self.__head
        str_ret = ""
        while start:
            if start.next_node:
                str_ret += str(start.data) + "\n"
            else:
                str_ret += str(start.data)
            start = start.next_node
        return str_ret

    def sorted_insert(self, value):
        """Inserts new node in the correct position(sorted)"""

        start = self.__head
        prev = None
        while start:
            if value < start.data:
                break
            prev = start
            start = start.next_node
        if prev:
            new_node = Node(value, prev.next_node)
            prev.next_node = new_node
        else:
            self.__head = Node(value, self.__head)
