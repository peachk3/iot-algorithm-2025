# 가장 효율적인 해저 케이블망 구성하기
from operator import itemgetter

# 전역 변수
G1 = None
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5
SIZE = len(cityAry) # 6

# 클래스 선언
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
    
# 그래프 출력
def printGraph(g):
    print('  ', end=' ')
    for v in range(g.SIZE):
        print(cityAry[v], end= ' ')
    print()
    for row in range(g.SIZE):
        print(cityAry[row], end=' ')
        for col in range(g.SIZE):
            print("%2d" % g.graph[row][col], end=' ') # %2d - 10진수 정수 2자리 출력
        print()
    print()

# 특정정점에 그래프가 연결되었는지 확인
def findVertex(g, findVtx):
    stack = []
    vistedAry = []

    current = 0 # 시작정점
    stack.append(current)
    vistedAry.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(SIZE):
            if g.graph[current][vertex] != 0:
                if vertex in vistedAry:
                    continue
                else:
                    next = vertex
                    break
        
        if next != None:
            current = next
            stack.append(current)
            vistedAry.append(current)
        else:
            current = stack.pop()
        
    if findVtx in vistedAry:
        return True
    else:
        return False
    
# 메인 코드
G = Graph(SIZE)
G.graph[서울][뉴욕] = 80; G.graph[서울][북경] = 10
G.graph[뉴욕][서울] = 80; G.graph[뉴욕][북경] = 40; G.graph[뉴욕][방콕] = 70
G.graph[런던][방콕] = 30; G.graph[런던][파리] = 60
G.graph[북경][서울] = 10; G.graph[북경][뉴욕] = 40; G.graph[북경][방콕] = 50
G.graph[방콕][뉴욕] = 70; G.graph[방콕][북경] = 50; G.graph[방콕][런던] = 30; G.graph[방콕][파리] = 20
G.graph[파리][방콕] = 20; G.graph[파리][런던] = 60

print('## 해저 케이블 연결을 위한 전체 연결도 ##')
printGraph(G)

# 가중치 간선 목록
edgeAry = []
for i in range(SIZE):
    for k in range(SIZE):
        if G.graph[i][k] != 0:
            edgeAry.append([G.graph[i][k], i, k])

# 가중치별 간선 내림차순 정렬
edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=False)

# 중복 간선 제거
newAry = []
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])

print('## 중복 간선 제거 목록 =>', end=' ')
print(newAry)

# 가중치 높은 간선부터 제거
index = 0
# 0:서울 1:뉴욕 2:런던 3:북경 4:방콕 5:파리
while len(newAry) > (SIZE - 1): # 간선의 수가 (정점수 -1) 될때까지 반복
    start = newAry[index][1] 
    end = newAry[index][2] 
    saveWeight = newAry[index][0] 

    G.graph[start][end] = 0 
    G.graph[end][start] = 0 
    
    startYN = findVertex(G, start) 
    endYN = findVertex(G, end) 

    if startYN and endYN: 
        del(newAry[index])
    else: 
        G.graph[start][end] = saveWeight
        G.graph[end][start] = saveWeight
        index += 1

# 결과 출력
print('## 최소비용 신장트리 결과 ##')
printGraph(G)