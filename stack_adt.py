# Plus: 각 리스트 값에 1씩 더해준다
# ex) 1 2 3 4 5 -> 2 3 4 5 6
# isReverse: 리스트를 거꾸로 바꿔준다
# ex) 1 2 3 None None -> None None 3 2 1
# Reset: 리스트 안을 다 None로 초기화 시켜주고 top을 -1로 함
# ex) 1 2 3 4 5 -> None None None None None


class Stack:
    stack_size = 10
    stack_list = [None] * stack_size
    top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.stack_size - 1:
            return True
        else:
            return False

    def push(self, e):
        if self.isFull() == True:
            print("배열이 가득 찼습니다")
            return 0

        self.top += 1
        self.stack_list[self.top] = e

    def pop(self):
        if self.isEmpty() == True:
            print("배열이 텅 비었습니다")
            return 0

        print(self.stack_list[self.top])
        self.stack_list[self.top] = None
        self.top -= 1

    def peek(self):
        print(self.stack_list[self.top])

    def isReverse(self):
        self.stack_list.reverse()
        return True

    def Reset(self):
        if self.isEmpty() == True:
            print("배열이 텅 비었습니다")
            return 0
        for i in range(-1, self.stack_size):
            self.stack_list[i] = None

        self.top = -1

    def Plus(self):
        if self.isEmpty() == True:
            print("배열이 텅 비었습니다")
            return 0
        for i in range(self.top, -1, -1):
            self.stack_list[i] += 1


stack = Stack()

print("push 확인")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.stack_list)
stack.Plus()
print(stack.stack_list)
stack.isReverse()
print(stack.stack_list)

stack.Reset()

print(stack.stack_list)
