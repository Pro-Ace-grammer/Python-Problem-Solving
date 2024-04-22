# Implementing Linked List in python
# This module contains the main linked list definition
# import this LinkedList class for use.

class Node:
    def __init__(self,  data=None):
        self.data = data
        self.next = None

class  LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)    # kind of nested class
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
