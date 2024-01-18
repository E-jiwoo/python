class Deque:
    def __init__(self, Deque_size):
        self.Deque_size = Deque_size
        self.front = -1
        self.rear = self.Deque_size
        self.list = [None] * self.Deque_size

    def isEmpty(self):
        return self.rear == self.Deque_size and self.front == -1

    def isFull(self):
        return self.front == self.Deque_size - 1 or self.rear == 0

    def AddFront(self, e):
        if self.isFull():
            print("덱이 가득 차있습니다")
        self.front += 1
        self.list[self.front] = e

    def DeleteFront(self):
        if self.isEmpty():
            print("덱이 비어있습니다")
        tmp = self.list[self.front]
        self.list[self.front] = None
        self.front -= 1
        return tmp

    def GetFront(self):
        return self.list[self.front]

    def AddRear(self, e):
        if self.isFull():
            print("덱이 가득 차있습니다")
            return 0
        self.rear -= 1
        self.list[self.rear] = e

    def DeleteRear(self):
        if self.isEmpty():
            print("덱이 비어있습니다")
            return 0
        tmp = self.list[self.rear]
        self.list[self.rear] = None
        self.rear += 1
        return tmp

    def GetRear(self):
        return self.list[self.rear]


deque = Deque(5)

deque.AddFront(1)
deque.AddFront(2)
deque.AddRear(1)
deque.AddRear(2)
print(deque.list)
