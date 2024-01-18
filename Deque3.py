class Deque:
    def __init__(self, Deque_size):
        self.Deque_size = Deque_size
        self.front = 0
        self.rear = 0
        self.list = [None] * Deque_size

    def isEmpty(self):  # front랑 rear가 같으면 비어있음
        return self.front == self.rear

    def isFull(self):  # front랑 (rear_1)%크기가 같으면 가득 참
        return self.front == (self.rear + 1) % self.Deque_size

    def Addfront(self, e):  # 맨 앞(전단)에 새로운 요소 e를 추가
        if self.isFull():
            print("덱이 가득 찼습니다")
            return 0
        self.list[self.front] = e
        self.front = (self.front - 1 + self.Deque_size) % self.Deque_size

    def Addrear(self, e):  # 맨 뒤(후단)에 새로운 요소e를 추가
        if self.isFull():
            print("덱이 가득 찼습니다")
            return 0
        self.rear = (self.rear + 1) % self.Deque_size
        self.list[self.rear] = e

    def Deletefront(self):  # 맨 앞(전단)의 요소를 꺼내서 반환
        if self.isEmpty():
            print("덱이 비어있습니다")
            return 0
        self.front = (self.front + 1) % self.Deque_size
        return self.list[self.front]

    def Deleterear(self):  # 맨 뒤(후단)의 요소를 꺼내서 반환
        if self.isEmpty():
            print("덱이 비어있습니다")
            return 0
        self.rear = (self.rear - 1 + self.Deque_size) % self.Deque_size
        return self.list[self.rear]

    def Getfront(self):  # 맨 앞(전단)의 요소를 꺼내지 않고 반환
        if self.isEmpty():
            print("덱이 비어있습니다")
            return 0
        return self.list[(self.front + 1) % self.Deque_size]

    def Getrear(self):  # 맨 뒤(후단)의 요소를 꺼내지 않고 반환
        if self.isEmpty():
            print("덱이 비어있습니다")
            return 0
        return self.list[self.rear]


deque = Deque(5)
deque.Addfront(1)
deque.Addfront(2)
deque.Addrear(2)
print(deque.list)
