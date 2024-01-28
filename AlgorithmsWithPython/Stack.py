class Stack:
    def __init__(self):
        self.element = []
    def IsEmpty(self):
        return len(self.element) == 0
    def peek(self):
        return self.element[-1]
    def push(self,data):
        self.element.append(data)
    def remove(self):
        if self.IsEmpty():
            return None
        else:
            return self.element.pop()
    def getSize(self):
        return len(self.element)

def main():
    myStack = Stack()
    myStack.push(24)
    myStack.push(34)
    myStack.push(12)
    myStack.push(78)
    myStack.push(48)
    myStack.push(18)
    myStack.push(98)
    myStack.push(34)

    while (myStack.getSize()>0):
        print(myStack.remove(),end=" ")

if __name__ == '__main__':
    main()