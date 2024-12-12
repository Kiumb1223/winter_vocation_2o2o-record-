# Python

[python网课学习第二周 图形的绘制](https://www.icourse163.org/learn/BIT-268001#/learn/content?type=detail&id=1212094119)

```python
#PythonDraw.py
import turtle   # import保留字  引入了一个绘图库名字叫：turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
	turtle.circle(40,80)
	turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
```

## turtle库概述

turtle（海龟）库是turtle绘图体系的Python实现

* turtle绘图体系：1969年诞生，主要用于程序设计入门
* Python语言的==标准库==之一
* 入门级的图形绘制函数库

==Python计算生态 \=  标准库 + 第三方库== 

- 标准库：随解释器直接安装到操作系统中功能模块
- 第三方库：需要经过安装才能使用的功能模块
- 库Library、包Package、模块Module,统称==模块== 	

## turtle 语法详解

* turtle 的**绘图窗体** 

```python
turtle.setup(width,height,startx,starty) 
```

1. setup（）设置窗体大小及位置

2. 参数：宽度，高度，起始点的xy方向   后两个可选

   宽度，高度指的是窗体本身的宽度，高度

   起始点是窗体左上角位置相对于屏幕坐标系中的屏幕左上角（零点）

   ```  python
   turtle.setup(800,400,0,0) #生成的窗体出现在屏幕坐标系的（0，0）坐标，即屏幕的左上角
   turtle.setup(800,400)     #生成的窗体出现在屏幕的正中央
   ```

3. setup()不是必须的  

   只有当你需要控制窗体的大小和在屏幕中显示位置的时候，才需要使用使用setup()函数

* turtle**空间坐标体系 **   包含绝对坐标和海龟坐标

  * 绝对坐标     turtle（海龟）最开始在画布的正中心——正中心的坐标是（0，0)

    ​					海龟的运行方向向着画布的右侧——整个窗体的右方向是X轴，上方向是Y轴

    ​					去利用绝对坐标体系，来改变turtle的行进位置。我们可以使用些函数叫==goto==

    ​					`turtle.goto(x,y) #它指的是让任何位置的海龟，去到达某一个坐标位置` 

     ```python
    #goto_using.py
    import turtle 
    turtle.goto(100,100)
    turtle.goto(100,-100)
    turtle.goto(-100,-100)
    turtle.goto(-100,100)
    turtle.goto(0,0)
     ```
    
  * 海龟坐标     它当前的行进方向，无论这个方向是朝向哪个角度的 ，叫做**前进方向** 
    
    ​					前进方向的反方向 是**后退方向** 
    
    ​					海龟运行的左侧叫做**左侧方向** 
    
    ​					海龟运行的右侧叫做**右侧方向** 
    
    ```python
    #海龟坐标体系的函数
    turtle.circle(r,angle)	
    #circle表示以海龟当前位置 左侧的某一个点为圆心 进行曲线运动
    turtle.fd(d)    #向海龟的正前方向运行d个像素
    turtle.bk(d)	#向海龟的反方向运行d个像素
    ```

* turtle的**角度坐标体系**

  * 绝对角度

    在空间坐标体系中的x轴表示**0**度或者**360** 度

  ​        Y轴表示**90** 度或者**-270** 度  以此类推形成了**绝对角度**的坐标体系

   		我们可以使用`turtle.seth(angle)`  

  ​								seth()改变海龟行进方向

  ​								seth()值改变方向但不行进

  ​								angle表示的是**绝对角度**

  * 海龟角度——更好的改变海龟的行进方向

    `turtle.left(angle)`  **海龟向左**

    `turtle.right(angle)` **海龟向右** 

* **RGB色彩体系** 

  * RGB指的是红蓝绿三个通道的颜色组合

  * 覆盖视力所能感知的所有颜色

  * RGB每色取值范围0-255整数或0-1小数

    我们这里使用`turtle.colormode(mode)`来改变色彩数值的使用 

    **默认采用小数值 可切换为整数值** 

    ```turtle
    turtle.colormode(1.0)  #采用RGB小数值模式
    turtle.colormode(255)  #采用RGB整数值模式
    ```

##  样例程序分析

* 库引用与import

  * 库应用      **扩充Python程序功能的方式**

    1. 使用==import==保留字完成，采用<a\>.<b\>()编码风格

       ==import==<库名\>

    ​        <库名\>.<函数名\>（<函数参数\>）

    2. import更多用法

       * 使用==form==和==import==保留字共同完成

         ==form==<库名>==import==<函数名>

         ==form==<库名>==import==*

         <函数名>(<函数参数>)

 ```python
#PythonDraw.py
from turtle import*
setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("purple")
seth(-40)
for i in range(4):
	circle(40,80)
	circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)
done()
​```
第一种方法不会出现函数重名问题
第二种方法会出现
​```
 ```

   3. 使用==import==和==as==保留字共同完成

      ==import==<库名>==as== <库别名>

      <库别名\>.<函数名>(<函数参数>)

      **给调用的外部库关联一个更短、更适合自己的名字**

      ```python
      
      import turtle as t
      t.setup(650,350,200,200)
      t.penup()
      t.fd(-250)
      t.pendown()
      t.pensize(25)
      t.pencolor("purple")
      t.seth(-40)
      for i in range(4):
      	t.circle(40,80)
      	t.circle(-40,80)
      t.circle(40,80/2)
      t.fd(40)
      t.circle(16,180)
      t.fd(40*2/3)
      t.done()
      ​```
      冗余的代码量最少
      防止库重名问题
      ​```
      ```

* 运动控制函数   **控制海龟行进：走直线&走曲线** 

  * turtle.forward(d)	别名	turtle.fd(d)

    向前行进，海龟走直线

    d:行进距离（像素），可以为负数

  * turtle.backward(d)    别名	turtle.bd(d)

  * turtle.circle(r,extent\===None==)

    根据半径r绘制extent角度的弧形

    r：默认圆心在海龟左侧r距离的位置       可以为负数

    extent：绘制角度，默认是360度整圆

* 方向控制函数  **控制海龟面对方向：绝对角度&海龟角度**

  * turtle.setheading(angle)    别名    turtle.seth(angle)

    改变行进方向，海龟走角度

    angle：改变行进方向，海龟走角度

  * turtle.left(angle)   海龟向左转

  * turtle.right(angle)   海龟向右转

    angle:在海龟当前行进方向上旋转的角度

* 循环语句中的**计数循环** 

  ==for==和==in==保留字       

  ==for==<变量>==in== range(<参数>)   其中的参数是循环次数

  ​	<被循环执行的语句>

  <变量>表示每次循环的计数，0到**<次数>-1**

```python
for i in range(5)
	print(i)
​```
输出
0
1
2
3
4
5
​```
```

​     range()函数   **产生循环计数序列**

​      range(N)    产生0到N-1的整数序列，共N个

​      range(M,N)  产生M到N-1的整数序列，共N-M个

* 画笔控制函数			将海龟想象成画笔

  

  **画笔操作一直有效，一般成对出现**

  * turtle.penup()     别名   turtle.pu()——抬起画笔，海龟在飞行
  * turtle.pendown()    别名  turtle.pd()——落下画笔，海龟在爬行

​     

​      **画笔设置后一直有效，直至下次重新设置**

   1. turtle.pensize(width)    别名   turtle.width(width)

      画笔宽度，海龟的腰围

2. turtle.pencolor(color) color为颜色字符串或r,g,b值

   画笔颜色，海龟在涂装

   **pencolor(color)的color参数可以有三种形式** 

   * 颜色字符串：`turtle.pencolor("purple")`

     purple是字符串形式而且要用小写

   * RGB的小数值：`turtle.pencolor(0.63,0.13,0.94)`

   * RGB的元组值：`turtle.pencolor((0.63,0.13,0.94))`

     元组值指的是将小数值或整数值形成一个独立的元素