import random

SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1


## 함수 선언 부분
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE):
        return True
    else :
        return False

def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False

# def push