"""
전위: +ab
중위: (a+b)/c
후위: ab+
"""
"""
중위를 후위로 바꿀 때 나올 수 있는 경우의 수 3가지
1. a+b*c -> abc*+
연산자를 담을 스택을 만들어 놓고 output이라는 결과를 순서대로 넣어놓는 리스트를 만든다
연산자는 stack에 넣고 피연산자는 output에 넣는다
stack에 든 게 있는 지 확인하고 
있다면
stack에서 한 개씩 pop해서 output에 넣어서 출력
2. a*b+c -> ab*c+ 
연산자를 담을 스택을 만들어 놓고 output이라는 결과를 순서대로 넣어놓는 리스트를 만든다
연산자는 stack에 넣고 피연산자는 output에 넣는다
stack에 넣을 연산자가 stack안에 들어있던 연산자랑 우선순위를 비교해서 stack에 있는 게 더 높은 우선순위가 있다면 
다 pop해서 output결과 리스트에 넣고 넣을 연산자를 stack에 집어 넣는다
다 분류했다면
stack에서 한 개씩 pop해서 output에 넣어서 출력
3. (a+b)*c ->
(를 stack에 집어넣는다
)괄호를 넣을 차례일 때 (를 만날 때까지 그 위에 들어있는 연산자를 모두 pop해서 output리스트에 넣어준다
다 분류했다면
stack에서 한 개씩 pop해서 output에 넣어서 출력
"""
# 피연산자인가 연산자인가 / 연산자에서 ()인가 +인가 *인가
"""
def 우선순위
if () return 0 
    + return 1
    * return 2
"""

# 스택 ADT

# push(e) : 요소 e를 스택의 맨 위에 추가
# pop() : 스택의 맨 위에 있는 요소를 꺼내 반환한다.
# isEmpty() : 스택이 비어있는 true를 아니면 false를 반환한다.
# isFull() : 스택이 가득 차 있으면 true를 아니면 false를 반환한다.
# peek() : 스택의 맨 위에 있는 항목을 삭제하지 않고 반환한다.


class Stack:
    stack_size = 100
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
        r = self.stack_list[self.top]
        self.stack_list[self.top] = None
        self.top -= 1
        return r

    def peek(self):
        print(self.stack_list[self.top])


# 연산자 우선순위 계산 함수
def precedence(op):
    if op == "(" or op == ")":
        return 0
    elif op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    else:
        return -1


# 중위 표기 -> 후위표기로 바꾸는 함수
def Infix2Postfix(expr):
    s = Stack()
    output = []

    for term in expr:
        if term in "(":
            s.push("(")
        elif term in ")":
            while not s.isEmpty():
                op = s.pop()
                if op == "(":
                    break
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(op) >= precedence(term):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output


"""
stack = Stack()

print("push 확인")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.stack_list)
"""
infix1 = input()
infix1 = list(infix1)
postfix1 = Infix2Postfix(infix1)
print(postfix1)
