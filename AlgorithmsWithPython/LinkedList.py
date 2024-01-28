class LinkedListIterator:
    def __init__(self,head):
        self.current = head
    def _next(self):
        if self.current == None:
            raise StopIteration
        Data  =self.current.Data
        self.current = self.current.Next
        return Data

class Node:
    def __init__(self,data):
        self.Data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def AddFirst(self,data):
        newNode = Node(data)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode.Next = self.head
            self.head = newNode
            self.size += 1
    
    def AddLast(self,data):
        newNode = Node(data)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.Next = newNode
            self.tail = newNode
            self.size += 1
    
    def _iter_(self):
        return LinkedListIterator(self.head)
    
    def Get_size(self):
        return self.size
    
    def RemoveFirst(self):
        self.head = self.head.Next

    def RemoveLast(self):
        if self.size == 0:
            return None
        if self.head.Next == None:
            self.head = None
            return None
        if self.size == 0:
            return None
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            last = self.head
            while last.Next.Next:
                last = last.Next
            self.tail = last
            last.Next = 0
            self.size -= 1
    
    def RemoveAtIndex(self,index):
        if index == 0:
            return self.RemoveFirst()
        elif index >= self.size:
            return self.RemoveLast()
        else:
            element = self.head
            for i in range(1,index):
                element = element.Next
            # temp = element.Next
            # element.Next = Node(data)
            element.Next = element.Next.Next
            self.size -= 1
    
    def Insert(self,index,data):
        if index == 0:
            return self.AddFirst()
        elif index >= self.size:
            return self.AddLast
        else:
            element = self.head
            for i in range(1,index):
                element = element.Next
            temp = element.Next
            element.Next = Node(data)
            element.Next.Next = temp
            self.size += 1
    
    def All(self):
        curr = self.head
        while curr != 0:
            print(curr.data)
            curr = curr.Next
    
    def IsEmpty(self):
        return self.size == 0
    
    def GetFirst(self):
        return self.head
    
    def GetLast(self):
        return self.tail
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.Data)
            curr = curr.Next
            if curr == 0:
                break

def main():
    myList = LinkedList()
    myList.AddFirst(2)
    myList.AddFirst(6)
    myList.AddFirst(10)
    myList.AddFirst(11)
    myList.print_list()

if __name__ == '__main__':
    main()