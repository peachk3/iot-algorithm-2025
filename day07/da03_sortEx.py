# 선택 정렬과 퀵 정렬 성능 비교
import random
import time

# 클래스, 함수 선언
# 선택 정렬
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k
        
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

# 큌 정렬
def qSort(arr, start, end):
    if end <= start:
        return
    
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

# 메인 코드
countAry = [1000, 10000, 12000, 15000]

for count in countAry:
    # countAry의 수만큼 랜덤한 숫자를 출력해서 배열에 넣기
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f'데이터 수 : {count}개')
    start = time.time()
    selectionSort(selectAry)
    end = time.time()
    print('선택 정렬 -> %10.3f 초' % (end - start))

    start = time.time()
    quickSort(selectAry)
    end = time.time()
    print('퀵 정렬 -> %10.3f 초' % (end-start))
    print()

    # count *= 5
    # print(count)
