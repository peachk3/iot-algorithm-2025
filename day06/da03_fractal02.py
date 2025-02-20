# 시에르핀스키 삼각형

from tkinter import *

## 함수선언
def drawTriangle(x, y, size):
    if size >= 30: # size >= 뒤숫자를 조정해서 결과 확인! -> 숫자가 클 수록 삼각형의 갯수는 작아짐
        drawTriangle(x, y, size/2) # 왼쪽 아래
        drawTriangle(x+size/2, y, size/2) # 오른쪽 아래
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2) # 중심 위쪽
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill='green', outline='green')

# 전역 변수
wSize = 1000
radius = 400

# 메인코드
root = Tk()
root.title('삼각형 모양의 프랙탈')
canvas = Canvas(root, height=wSize, width=wSize, bg="white")

drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
root.mainloop()