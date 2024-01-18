"""
AllPrint(): None이 아닌 배열에 있는 수 모두 출력
ex) [1, 2, 3, 4, None] -> [1, 2, 3, 4]가 출력됨
AllPrintReverse(): None이 아닌 배열에 있는 수 거꾸로 하여 모두 출력
ex) [1, 2, 3, 4, None] -> [4, 3, 2, 1]가 출력됨
Reset(): 배열 초기화
ex) 1, 2, 3, 4, None -> None, None, None, None, None
"""


class Queue:
    def __init__(self, size):
        self.queue_size = size
        self.list = [None] * self.queue_size
        self.rear = 0
        self.front = 0

    def isEmpty(self):  # front랑 rear가 같으면 비어있음
        return self.front == self.rear

    def isFull(self):  # (rear+1)%5랑 front가 같으면 가득 차 있음
        return (self.rear + 1) % 5 == self.front

    def equence(self, e):  # 요소 e를 큐의 맨 뒤에 추가
        if self.isFull():
            print("큐가 가득 찼습니다")
            return 0
        self.rear = (self.rear + 1) % 5
        self.list[self.rear] = e

    def dequence(self):  # 큐의 맨 앞에 있는 요소를 꺼내 반환
        if self.isEmpty():
            print("큐가 비어있습니다")
            return 0
        self.front = (self.front + 1) % 5
        self.list[self.front] = None
        return self.list[self.front]

    def peek(self):  # 큐의 맨앞에 있는 요소를 삭제하지 않고 반환
        if self.isEmpty():
            print("큐가 비어있습니다")
        return self.list[(self.front + 1) % 5]

    def AllPrint(self):  # 배열에 있는 수 모두 출력
        if self.isEmpty():
            print("큐가 비어있습니다")
            return 0
        tmp = [i for i in self.list if i is not None]
        print(tmp)

    def AllPrintReverse(self):  # 배열에 있는 수 거꾸로 하여 모두 출력
        if self.isEmpty():
            print("큐가 비어있습니다")
            return 0
        tmp = [i for i in self.list if i is not None]
        print(tmp[::-1])

    def Reset(self):  # 배열 초기화
        if self.isEmpty():
            print("큐가 비어있습니다")
            return 0
        for i in range(-1, self.queue_size):
            self.list[i] = None
        self.front = 0
        self.rear = 0


queue = Queue(5)

print("push 확인")
queue.equence(1)
queue.equence(2)
queue.equence(3)
queue.equence(4)
queue.dequence()
print(queue.peek())
queue.AllPrint()
queue.AllPrintReverse()

""" 오늘 수업에서 알게된 점
큐에는 
선형큐, 원형큐, 우선수위 큐 이렇게 세가지로 있다!
"""
