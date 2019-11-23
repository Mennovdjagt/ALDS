class myStack:

    def __init__(self):
        self.arr = []

    def push(self, x):
        """function that adds an item to the top of the list

        Args:
            x: the element we want to add to the list

        Examples:
            >>> stack.push(5)
            arr = [5]

        """
        self.arr.append(x)

    def pop(self):
        """function that returns and removes the item on top of the list

        Returns:
            x: the item at the end of the list, that we just deleted

        Examples:
            arr = [5]
            >>> stack.pop()
            arr = []

        """
        x = self.arr[-1]
        del self.arr[-1]
        return x

    def peek(self):
        """function that returns the item on top of the list without removing it

        Returns:
            x: the last element in the array

        Examples:
            arr = [1, 2, 3, 4, 5]
            >>> print(stack.peek())
            5

        """
        return self.arr[-1]

    def isEmpty(self):
        """function that returns whether myStack contains any items

        Args:
            x (bool): returns True if there is something in the list, False if array is empty

        Examples:
            arr = []
            >>> print(stack.isEmpty())
            False

            arr = [1, 2, 3, 4, 5]
            >>> print(stack.isEmpty())
            True

        """
        if not self.arr:
            return False
        else:
            return True

stack = myStack()
stack.push(5)
print(stack.peek())
print(stack.pop())
print(stack.isEmpty())
stack.push(5)
print(stack.isEmpty())
print(stack.peek())


