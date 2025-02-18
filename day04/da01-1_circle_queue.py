# 원형 큐 실습
# 초기화
SIZE = int(input('큐 크기 입력 >'))
queue = [None for _ in range(SIZE)]
front = rear = 0

def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear + 1) % SIZE) == front:
        # -> ㄷ                        
        return True
    else :
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear :
        return True
    else:
        return False

def eunQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() :
        print('Queue is full')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def delQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peekQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    return queue[(front + 1) % SIZE]


if __name__ == '__main__':
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) -->').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            eunQueue(data)
            print(f'큐 상태 > {queue}')
        elif select == 'E':
            data = delQueue()
            print(f'입력 데이터 > {data}')
            print(f'큐 상태 > {queue}')
        elif select == 'V':
            data = peekQueue()
            print(f'입력 데이터 > {data}')
            print(f'큐 상태 > {queue}')
        else:
            print('입력 오류')
            
print('프로그램 종료')