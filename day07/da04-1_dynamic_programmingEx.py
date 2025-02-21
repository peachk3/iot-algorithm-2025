# 황금 미로에서 길 표시하기
# 클래스 함수 선언
def printMaze(arr):
    for i in range(row):
        for k in range(col):
            print('%3d' % arr[i][k], end=' ')
        print()
    print()

def growRich():
    memo = [[0 for _ in range(col)] for _ in range(row)]
    memo[0][0] = goldMaze[0][0]

    colSum = memo[0][0]
    for i in range(1, col):
        colSum += goldMaze[i][0]
        memo[i][0] = colSum
    
    rowSum = memo[0][0]
    for i in range(1, row):
        rowSum += goldMaze[0][i]
        memo[0][i] = rowSum
    
    for ROW in range(1, row):
        for COL in range(1, len(goldMaze[ROW])):
            if (memo[ROW][COL-1] > memo[ROW-1][COL]):
                memo[ROW][COL] = memo[ROW][COL-1] + goldMaze[ROW][COL]
            else:
                memo[ROW][COL] = (memo[ROW-1][COL] + goldMaze[ROW][COL])
    
    retValue = memo[row-1][col-1]

    print('## 메모이제이션 ##')
    printMaze(memo)

    ROW, COL = row-1, col-1
    memo[ROW][COL] = 0
    while ROW != 0 or COL != 0:
        if ROW-1 >= 0 and COL-1 >= 0:
            if memo[ROW-1][COL] > memo[ROW][COL-1]:
                ROW -= 1
            else:
                COL -= 1
        elif ROW-1 < 0 and COL-1 >= 0:
            COL -= 1
        else:
            ROW -= 1
        memo[ROW][COL] = 0
    
    print('## 메모이제이션(황금 미로 길) ##')
    printMaze(memo)

    return retValue

# 전역 변수
row, col = 5, 5
goldMaze = [[1, 4, 4, 2, 2],
            [1, 3, 3, 0, 5],
            [1, 2, 4, 3, 0],
            [3, 3, 0, 4, 2],
            [1, 3, 4, 5, 3]]

macolGold = growRich()
print(f'얻은 최대 황금 개수 -> {macolGold}')