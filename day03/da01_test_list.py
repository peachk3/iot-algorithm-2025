# 단순 연결 리스트 실습 (p.149)
memory = []
head, prev, curr = None, None, None 
dataArray = [
    ['지민', '010-1111-1111'],
    ['정국', '010-2222-2222'],
    ['뷔', '010-3333-3333'],
    ['슈가', '010-4444-4444'],
    ['진', '010-5555-5555']
]

class Node():
    def __init__(self):
        self.data = None
        self.link = None
    

def printNodes(start):
    curr = start
    if curr == None:
        return
    print(curr.data, end=' ')

    while curr.link != None:
        curr = curr.link
        print(curr.data, end=' ')
    print()

def makeSimpleLinkedList(namePhone):
    global memory, head, prev, curr
    printNodes(head)

    node = Node()
    node.data = namePhone
    memory.append(node)
    if head == None :
        head = node
        return

    if head.data[0] > namePhone[0]:
        node.link = head
        head = node
        return
    
    # 중간 노드로 삽입하는 경우
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data[0] > namePhone[0]:
            prev.link = node
            node.link = curr
            return

    # 삽입하는 노드가 가장 큰 경우
    curr.link = node

if __name__ == '__main__':

    for data in dataArray:
        makeSimpleLinkedList(data)
    
    printNodes(head)