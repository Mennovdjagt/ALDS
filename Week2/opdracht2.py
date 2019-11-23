class myStack:

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        x = self.arr[-1]
        del self.arr[-1]
        return x

    def peek(self):
        return self.arr[-1]

    def isEmpty(self):
        if not self.arr:
            return False
        else:
            return True


b = "(<>)[]()(()())"
opening = "<([{"
closing = ">)]}"
stack = myStack()

for i in b:
    if i in opening:                #check if a char of b is equal to opening
        stack.push(i)
    elif i in closing:              #check if a char of b is equal to closing
        tmp = stack.peek()
        if opening.index(tmp) == closing.index(i):      #checks if the last elements position is equal to the closing position of i
            stack.pop()

if not stack.isEmpty():
    print("valid")
else:
    print("invalid")
