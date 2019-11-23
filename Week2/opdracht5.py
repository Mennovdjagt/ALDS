class node:

    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None
        self.tail


    def append(self, value):
        newNode = node(value)
        newNode.next = self.head
        self.head = newNode


    def delete(self, value):
        #do more shit


    def min(self):
        #do even more shit


