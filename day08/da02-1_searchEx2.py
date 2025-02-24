# 편의점에서 판매된 물건 목록과 개수 세기

import random

# 클래스, 함수 선언
def binSearch(ary, fData):
    start = 0
    end = len(ary) - 1

    while start <= end :
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# 전역 변수
dataAray = ['바나나우유', '레쓰비캔커피', '츄파풉스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sellAry = [random.choice(dataAray) for _ in range(20)]

# 메인 코드
print(f'오늘 판매된 전체 물건(중복 O, 정렬 X) -> {sellAry}')
sellAry.sort()
print(f'오늘 판매된 전체 물건(중복 O, 정렬 O) -> {sellAry}')
sellProduct = list(set(sellAry))
print(f'오늘 판매된 물품 종류(중복 X) -> {sellProduct}')

countList = []
for product in sellProduct:
    count = 0
    pos = 0
    while (pos != -1):
        pos = binSearch(sellAry, product)
        if pos != -1:
            count += 1
            del(sellAry[pos])
    countList.append((product, count))

print()
print(f'결산 결과 => {countList}')