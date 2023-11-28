Deque_size = 5
list = [None] * Deque_size
front = -1
rear = -1


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


def Addfront(e):
    global front
    if isFull():
        print("큐가 가득 찼습니다")
        return 0
    front = (front + 1) % 5
    list[front] = e


def Deletefront():
    global front

    if isEmpty() == True:
        print("배열이 비어있습니다")
        return 0

    print(list[front])
    list[front] = None


def Getfront():
    global rear, front
    print(list[rear])


def Addrear(e):
    global rear

    if isFull() == True:
        print("배열이 가득 차있습니다")
        return 0

    rear -= 1
    rear = Deque_size
    list[rear] = e


def Deleterear():
    global rear

    if isEmpty() == True:
        print("배열이 비어있습니다")
        return 0

    print(list[rear])
    list[rear] = None
    rear -= 1


def Getrear():
    global front
    print(list[front])


print("Addfront 확인")
Addfront(1)
Addfront(2)

print("Addrear 확인")
Addrear(1)
Addrear(2)


print(list)
