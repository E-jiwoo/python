queue_size = 5
list = [None] * queue_size
rear = 0
front = 0


def isEmpty():
    global rear, front

    if front == rear:
        return True
    return False


def isFull():
    global rear, front

    if (rear + 1) % 5 == front:
        return True
    return False


def equence(e):
    global rear, front

    if isFull():
        print("큐가 가득 찼습니다")
        return 0
    rear = (rear + 1) % 5
    list[rear] = e


def dequence():
    global rear, front

    if isEmpty():
        print("큐가 비어있습니다")
        return 0
    list[rear] = None
    rear = (rear + 1) % 5


def peek():
    global rear, front
    print(list[rear])


print("push 확인")
equence(1)
equence(2)
equence(3)
equence(4)

print(list)

print("pop 확인")
dequence()
dequence()
dequence()

equence(6)

print(list)

""" 오늘 수업에서 알게된 점
큐에는 
선형큐, 원형큐, 우선수위 큐 이렇게 세가지로 있다!
"""
