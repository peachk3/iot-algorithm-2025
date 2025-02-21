# 이미 정렬된 줄에 끼어들기
import random
import time

# 클래스, 함수 선언
# 버블 정렬
def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if (ary[cur] > ary[cur + 1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
        if not changeYN:
            break
    return ary

# 퀵 정렬
def qSort(arr, start, end):
    if end <= start: return

    low = start
    high = end

    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    mid = low

    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

def quickSort(ary):
    qSort(ary, 0, len(ary) - 1)

tempAry = [random.randint(10000, 99999) for _ in range(1000000)]
tempAry.sort()

rndPos = random.randint(0, len(tempAry)-1)
print(f'# 데이터 개수 --> {len(tempAry)}')
print(f'# 끼어든 위치 --> {rndPos}')
tempAry.insert(rndPos, tempAry[-1])

bubbleAry = tempAry[:]
quickAry = tempAry[:]

start = time.time()
bubbleSort(bubbleAry)
end = time.time()
print('다시 정렬 시간(버블 정렬) --> %10.3f 초' % (end-start))

start = time.time()
quickSort(quickAry)
end = time.time()
print('다시 정렬 시간(퀵 정렬) --> %10.3f 초' % (end-start))