class Queue:
    def __init__(self, size):
        self.queue_size = size
        self.list = [None] * self.queue_size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.rear == self.queue_size - 1

    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, e):
        if self.isFull():
            print("큐가 포화상태입니다")
            return 0
        self.rear = self.rear + 1
        self.list[self.rear] = e

    def dequeue(self):
        if self.isEmpty():
            print("큐가 공백상태입니다")
            return -1
        self.front = self.front + 1
        tmp = self.list[self.front]
        self.list[self.front] = None
        return tmp

    def peek(self):
        if self.isEmpty():
            print("큐가 공백상태입니다")
        return self.list[self.front + 1]

    def AllPrint(self):
        if self.isEmpty():
            print("큐가 공백상태입니다")
            return 0
        tmp = [i for i in self.list if i is not None]
        print(tmp)

    def AllPrintReverse(self):
        if self.isEmpty():
            print("큐가 공백상태입니다")
            return 0
        tmp = [i for i in self.list if i is not None]
        print(tmp[::-1])

    def Reset(self):
        if self.isEmpty():
            print("큐가 공백상태입니다")
            return 0
        for i in range(-1, self.queue_size):
            self.list[i] = None

        self.front = -1
        self.rear = -1


queue = Queue(5)

queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)
queue.enqueue(1)

print(queue.list)
print(queue.peek())
queue.Reset()
print(queue.list)
