# 2차원 배열의 중앙값 찾기

# 전역변수 선언
ary2 = [[55, 33, 250, 44],
        [88, 1, 67, 23],
        [199, 222, 38, 47],
        [155, 145, 20, 99]]

ary1 = []

# 클래스, 함수 선언
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k
            
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    
    return ary

# 메인 코드 
# ary2 2차원 배열의 값을 ary1에 넣어주기
for i in range(len(ary2)):
    for k in range(len(ary2[i])):
        ary1.append(ary2[i][k]) 
        # print(ary1) 

print(f'1차원 변경 후, 정렬 전 -> {ary1}')
ary1 = selectionSort(ary1)
print(f'1차원 변경 후, 정렬 후 -> {ary1}')
print(f'중앙값 -> {ary1[len(ary1)//2]}')
