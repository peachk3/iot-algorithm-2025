# 큐 자료구조 구현

# 초기화
SIZE = int(input('큐 크기 입력 > '))
queue = [None for _ in range(SIZE)]
front = rear = -1

# 함수 선언
def isQueueFull():
    global SIZE, queue, front, rear # -> def 안에서만 전역변수의 값을 바꾸려고 할 때만 사용
    # 1. 가장 일반적 로직 -> 큐에서 모든 데이터를 추출한 후에 입력 시 입력 불가능
    # if rear == SIZE - 1:
    #     return True
    # else:
    #     return False
    
    # 2.개선 로직 -> 큐에서 모든 데이터 추출 후 재입력 가능 (뒤에서부터 입력됨)
    if rear != SIZE - 1:
        return False
    elif rear == SIZE - 1 and front == -1:
        return True
    else:
        for i in range(front + 1, SIZE):
            queue[i - 1] = queue[i] # 데이터 앞의 빈자리에 첫번째 데이터 옮김
            queue[i] = None
        
        front -= 1
        rear -= 1
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is full')
    else:
        rear += 1
        queue[rear] = data

def delQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data

def peekQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        return queue[front + 1]
    
## 메인 모듈
if __name__ == '__main__':
    # print('메인 선언!') -> 초기화 input 먼저 실행되고 나서 메인 모듈 실행됨
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) --> ').upper()
        
        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select == 'E':
            data = delQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select == 'V':
            data = peekQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        else:
            print('입력 오류')
