from tkinter import *
import random

def drawCircle(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    if r >= 5: # 숫자가 커질수록 원의 갯수 줄어듬!!
        drawCircle(x+r//2, y, r//2)
        drawCircle(x-r//2, y, r//2)

colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet']
wSize = 1000
radius = 400

root = Tk()
root.title('원 모양의 프랙탈')
canvas = Canvas(root, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
root.mainloop()