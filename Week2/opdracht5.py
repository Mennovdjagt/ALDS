class linkedList:

    def __init__(self, value = None):
        self.value = value
        self.tail = None

    def append(self, value):
        if self.value == None:
            self.value = value
            return
        if self.tail == None:
            self.tail = linkedList(value)
            return
        self.tail.append(value)

    def delete(self, value):
        if self.tail == None:
            return
        if self.value == value:
            self.value = self.tail.value
            self.tail = self.tail.tail
        self.tail.delete(value)

    def min(self):
        if self.tail != None:
            return self.value
        tmp = self.tail.min()
        if tmp < self.value:
            return tmp
        return self.value

    def print(self):
        print(self.value)
        if self.tail != None:
            self.tail.print()


x = linkedList()

x.append(8)
x.append(9)
x.append(10)
x.print()
x.delete(8)
x.append(11)
print("min: ", x.min())
x.print()
