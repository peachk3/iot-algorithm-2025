# 기본 정렬 알고리즘 응용

def selectionSort(ary) :
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

# 전역변수 선언
moneyAry = [7, 5, 11, 6, 9, 80000, 10, 6, 15, 12]

# 메인 코드
print(f'용돈 정렬 전 -> {moneyAry}')
moneyAry = selectionSort(moneyAry)
print(f'용돈 정렬 후 -> {moneyAry}')
print(f'용돈 중앙값 -> {moneyAry[len(moneyAry)//2]}')


import os
# fnameAry = []
folderName = 'C:/Windows/System32'
# for dirName, subDirList, fnames in os.walk(folderName):
#     for fname in fnames:
#         fnameAry.append(fname)

# print(len(fnameAry))


def makeFileList(floderName):
    fnameAry = []
    for dirName, subDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname)
    return fnameAry

def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur-1]<ary[cur]):
                ary[cur-1],ary[cur] = ary[cur], ary[cur-1]
    return ary

fileAry = []

fileAry = makeFileList('C:/Program Files/Common Files')
fileAry = insertionSort(fileAry)
print(f'파일명 역순 정렬 -> {fileAry}')
