from LinkedList import LinkedList
class Queue:
    def __init__(self):
        self.element = LinkedList()
    def isEmpty(self):
        return self.element.IsEmpty()
    def getSize(self):
        return self.element.Get_size()
    def Enqueue(self,data):
        return self.element.AddFirst(data)
    def Dequeue(self):
        return self.element.RemoveFirst()
    
def main():
    myQueue = Queue()
    myQueue.Enqueue(1)
    myQueue.Enqueue(2)
    myQueue.Enqueue(3)
    myQueue.Enqueue(4)
    myQueue.Enqueue(5)
    myQueue.Enqueue(6)
    while myQueue.getSize()>0:
        print(myQueue.Dequeue(),end=' ')

main()