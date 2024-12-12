[toc]

## 函数的定义

> 函数是一段代码的表示

* 函数是一段具有特定功能的，可重用的语句组

* 函数是一种功能的抽象，一般函数表达特定功能

* 两个作用:==降低编程难度== 和==代码复用== 

  

==def==   <函数体>==(==  <参数(0个或多个)>==)==

​		<函数体>

​		==return==  <返回值>



* 函数定义时，所指定的参数是一种**占位符**

* 函数定义后，如果不经过**调用**，不会被执行
* 函数定义时，参数是输入，函数体是处理，结果是输出（IPO）

## 函数的使用及调用过程

* 函数的调用   **调用是运行函数代码的方式**
  * 调用时要给出实际参数
  * 实际参数替换定义中的参数
  * 函数调用后得到返回值

## 函数的参数传递

* **函数可以有参数，也可以没有，但必须保留括号** 

* **函数定义时可以为某些参数指定默认值，构成可选参数**

  ==def==   <函数体>==(==  <非可选参数>，<可选参数>==)==

  ​		<函数体>

  ​		==return==  <返回值>

  * 可选参数放在非可选参数之后

* 可变参数传递

  * **函数定义时可以设计可变数量参数，即不确定参数总数量** 

    ==def==   <函数体>==(==  <参数>，\*b==)==			#b可以任意名字，重点在于*号

    ​		<函数体>

    ​		==return==  <返回值>

* 参数传递的两种方式

  * 函数调用时，参数可以按照位置或者名称方式传递

    ```python
    def fact (n,m=1):
        s=1
        for i in range (1,n+1):
            s*=i
        return s//m
    >>>fact (10,5)#位置传递
    725760
    >>>fact (m=5,n=10)#名称传递
    725760        
    ```

* 函数的返回值   **函数可以返回0个或多个结果** 

  * ==return== 保留字用来传递返回值

  * 函数可以有返回值，也可以没有，可以有==return== ，也可以没有

  * ==return== 可以传递0个返回值，也可以传递任意多个返回值

    ```python
    def fact (n,m=1):
        s=1
        for i in range (1,n+1):
            s*=i
        return s//m,n,m
    >>> fact (10,5)
    (725760,10,5)      #元组类型——组合数据类型
    >>> a,b,c = fact(10,5)
    >>>print(a,b,c)
    725760 10 5
    ```

## 局部变量和全局变量

* ==局部变量和全局变量是不同变量== 

  * 局部变量是函数内部的占位符，与全局变量可能重名但不同

  * 函数运算结束后，局部变量被释放

  * 可以使用==global==保留字在函数内部使用全局变量

    ```python 
    n,s=10,100
    def fact (n):
        global s   #fact()函数中使用global保留字，声明此处s是全局变量s
        for i in range (1,n+1):
            s*=i
        return s   #此处s是指全局变量s
    print (fact(n),s)  #此处全局变量s被函数修改
    ```

* ==局部变量为组合数据类型且未创建，等同于全局变量== 

  ```python 
  ls =['F','f']
  def func(a):
      ls.append(a)
      return 
  func("C")
  print(ls)
  ```

## lambda函数

> lambda函数返回函数名作为结果

* lambda函数是一种匿名函数，既没有名字的函数

* 使用==lambda==保留字定义，函数名返回结果

* lambda函数用于定义简单的、能够在一行内表示的函数

  `<函数名> = lambda <参数> : <表达式>`     这是一种非常简单函数的紧凑表达形式

  ```python 
  >>> f = lambda x,y :x+y
  >>> f(10,5)
  15
  >>> f=lambda:"lambda函数"
  >>> print(f())
  lambda函数
  ```

* **谨慎使用lambda函数** 

  * lambda函数主要用作一些特定函数或方式的参数
  * lambda函数有一些固定使用方式，建议逐渐掌握
  * 一般情况下，建议使用==def== 定义的普通函数

##  实例   七段数码管代码

```python 
import turtle
import time
turtle.speed(10)
def drawGap():   #增加空隙
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,9] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,5,6,7,8,9]  else  drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date :
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)  #????
        elif i == '=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))#获取系统时间
    turtle.hideturtle()    #隐藏箭头显示
    turtle.done()
main()                                                    
```



## 代码复用

> 把代码当成资源进行抽象

* **代码资源化** ：程序代码是一种用来表达计算的”资源“
* **代码抽象化** ：使用函数等方法对代码赋予更高级别的定义
* **代码复用** ：同一份代码在需要时可以被重复使用

> 函数和对象 是代码复用的两种主要形式

* **函数** ： 将代码命名

  在代码层面建立了初步抽象

* **对象** ：属性和方法

  <a\>.<b\>和<a\>.<b\>()

  在函数之上再次组织进行抽象

## 模块化设计

> 分而治之

* 通过函数或对象封装将程序划分为模块及模块间的表达
* 具体包括：主程序，子程序和子程序间的关系
* 分而治之：一种分而治之、分层抽象、体系化的设计思想

> 紧耦合  松耦合

* **紧耦合** ： 两个部分之间交流很多，无法独立存在
* **松耦合** ：两个部分之间交流很少，可以独立存在
* 模块内部紧耦合，模块之间松耦合

## 递归

> 函数定义中调用函数自身的方式

namely  
$$
n!=
	\begin{cases}
	1  & n=0  \\
	{n(n-1)!}  &otherwise
	\end{cases}
$$

> 两个关键特征

* **链条** ：计算过程存在递归链条

  如$n!={n(n-1)!}$	

* **基例** ：存在一个或多个不需要再次递归的基例  

  如$n!=1$

> 类似数学归纳法

##  递归的实现

> 函数 + 分支语句

* 递归本身是一个函数，需要函数定义方式描述
* 函数内部，采用分支语句对输入参数进行判断
* 基例和链条，分别编写对应代码

例子：

 ```python 
# 实现字符串s反转
def rvs (S):
    if s='':       #基例
        return s
    else: 
        return rvs(s[1:])+s[0]    #链条
 ```

斐波那契数列
$$
f(n)=
	\begin{cases}
	 1          & n=1\\
	 1          & n=2 \\
	 f(n-1)+f(n-2)&otherwise
	 \end{cases}
$$

```python 
def fun(n):
    if n == 1 or n == 2 :
        return 1
    else : 
        return f(n-1)+f(n-2)
```

汉诺塔问题

```python 
count = 0
def hanoi (n,src,dst,mid):   #src 指的是起始柱子，dst指的是目标柱子  mid指的是过渡柱子
    global count 
    if n == 1:
        print("{}->{}->{}".format(1,src,dst))
        count +=1
    else :
        hanoi(n-1,src,mid,dst)
        print("{}->{}->{}".format(n,src,dst))
        count +=1
        hanoi(n-1,mid,dst,src)
```

 ## PyInstaller库

> 将.py源代码转换成无需源代码的可执行文件

```flow
st=>inputoutput: .py文件
po=>operation: Pyinstaller
en=>inputoutput: 1.window 2.Linux 3.Mac OS X
st(right)->po(right)->en
```

* Pyinstaller库是第三方库
  * 官方网站：http://www.pyinstaller.org
  * 第三方库：使用前需要额外安装
  * 安装第三方库需要使用pip工具

* Pyinstaller库常用参数

  | 参数                | 描述                               |
  | ------------------- | ---------------------------------- |
  | -h                  | 查看帮助                           |
  | --clean             | 清理打包过程中的临时文件           |
  | -D,--onedir         | 默认值，生成dist文件夹             |
  | -F，--onefile       | 在dist文件夹只生成独立的打包文件   |
  | -i <图标文件名.ico> | 指定打包程序使用的图标（icon）文件 |

## 科赫雪花小包裹

* 科赫雪花   ==高大上的分形几何== 
  * 分形几何是一种迭代的几何图形，广泛存在于自然界

<table>
    <tr>
    <td><center>
        <img src="http://www.pep.com.cn/oldimages/pic_238858.gif">图一 分形几何
        </center>
    </td>
        <td><center>
            <img src="https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=946bc2d6d143ad4bb2234e92e36b31ca/359b033b5bb5c9ea58963c90d539b6003af3b35f.jpg">图二  科赫雪花图解
            </center>
    </td>
    </tr>
</table>

* 用python编写科赫**曲线** 

  * 详情见图二

  * ```python 
    #KochDrawV1.py
    import turtle 
    def koch (size,n):  #size 表示直线的长度size  n表示我们希望绘制的阶数n
        if n==0:
            turtle.fd(size)
        else:
            for angle in [0,60, -120,60]:
                turtle.left(angle)
                koch(size/3,n-1)
    def main():
        turtle.setup(800,400)
        turtle.penup()
        turtle.goto(-300,-50)
        turtle.pendown()
        turtle.pensize(2)
        koch(600,3)   #3阶科赫曲线 ，阶数
        turtle.hideturtle()
    main()
    ```

  * 我们着重理解该递归的链条：

    * 将一条直线切分为三段，中间这一段去掉，然后我们让中间绘制一个凸起的三角形
    * 如果再进一阶是把其中的每一个线段 ，做下一次的科赫曲线的绘制，如此一来我们可以对n阶和n-1阶的科赫曲线做一个链条

* 用python绘制科赫**雪花**

  * ```python 
    #KochDrawV1.py
    import turtle 
    def koch (size,n):  #size 表示直线的长度size  n表示我们希望绘制的阶数n
        if n==1:
            turtle.fd(size)
        else:
            for angle in [0,60 ,-120,60]:
                turtle.left(angle)
                koch(size/3,n-1)
    def main():
        turtle.setup(600,600)
        turtle.penup()
        turtle.goto(-200,100)
        turtle.pendown()
        turtle.pensize(2)
        level = 3 #3阶科赫雪花，阶数
        #这里是一个等边三角形，如图二中的三角形，边长400像素
        koch(400,level)
        turtle.right(120)
        koch(400,level)
        turtle.right(120)
        koch(400,level)
        turtle.hideturtle()    
    main()
    ```

