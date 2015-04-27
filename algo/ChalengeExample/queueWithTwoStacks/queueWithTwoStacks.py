
class StackWithTwoQueues():

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.insert(0,val)

    def dequeue(self):
        while len(self.stack1):
            self.stack2.insert(0,self.stack1.pop())
        val = self.stack2.pop()
        self.stack1 = []
        while len(self.stack2):
            self.stack1.insert(0,self.stack2.pop())
        return val

    def printStack1(self):
        i = 0
        while i < len(self.stack1) :
            print(self.stack1[i])
            i += 1

if __name__ == '__main__':
    s =  StackWithTwoQueues()
    s.enqueue(12)
    s.enqueue(13)
    s.enqueue(14)
    s.enqueue(15)
    s.printStack1()
    print("DEQUE",s.dequeue())
    s.printStack1()
    print("DEQUE",s.dequeue())
    s.printStack1()
    print("DEQUE",s.dequeue())
