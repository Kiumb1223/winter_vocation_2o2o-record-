import turtle as t
import time
t.speed()
#绘制五角星
#(startx，starty)为五角星中心点的坐标
def StarDraw(startx,starty,line):
    t.penup()
    t.goto(startx,starty)
    t.pendown()
    t.setheading(90)
    t.fd(line/2)
    t.right(162)
    t.color("yellow","yellow")
    t.begin_fill()
    for i in range(5):
        t.fd(line)
        t.right(144)
    t.end_fill()
#绘制国旗
t.penup()
t.goto(-150,100)
t.pendown()
t.color("black","red")
t.begin_fill()
for i in range(2):
    for j in [300,200]:
        t.fd(j)
        t.right(90)
t.end_fill()
#绘制星星
StarDraw(-100,50,60)
StarDraw(-50,80,20)
StarDraw(-30,60,20)
StarDraw(-30,30,20)
StarDraw(-50,10,20)

#武汉加油，中国加油！
t.penup()
t.goto(-50,-150)
t.pendown()
t.hideturtle()
t.pencolor("red")
t.write("武汉加油!中国加油！",font=(50))
time.sleep(2)
t.done()

