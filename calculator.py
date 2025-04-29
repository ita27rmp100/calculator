from tkinter import *
t = Tk()
t.title("الآلةالحاسبة")
t.geometry("190x210")
t.resizable(1,1)
t.configure(bg="black")
rt = StringVar()
e = 2.7182818285
π = 3.1415926235
h = IntVar()
from math import *
def n(n) :
    rt.set(rt.get()+n)
def r() :
    try :
        u = eval(rt.get())
        rt.set(round(u,6))
    except :
        u = "error"
        rt.set(u)
def c() :
    rt.set("")
def ed() :
    bn = len(rt.get())-1
    x = rt.get()
    n = x[0:bn]
    rt.set(str(n))
def devl() :
    t.geometry("190x350") #الآلة الحاسبة تكون علمية
def bat() : #الآلة الحاسبة تكون بسيطة
    t.geometry("190x190")
# btns
amalia = Label(t,textvariable=rt,font=("arial",15),width="16",bd=0,height="1",bg="lightblue",fg="white").place(x=5,y=7)
kisma = Button(t,text="/",command=lambda :n("/"),bg="orange",height="1",width="3").place(x=5,y=35)
tharb = Button(t,text="*",command=lambda :n("*"),bg="orange",height="1",width="3").place(x=40,y=35)
nakis = Button(t,text="-",command=lambda :n("-"),bg="orange",height="1",width="3").place(x=75,y=35)
zaaid = Button(t,text="+",command=lambda :n("+"),bg="orange",height="1",width="3").place(x=110,y=35)
clear = Button(t,text="C",command=c,bg="orange",height="1",width="5").place(x=140,y=70)
c1 = Button(t,text="(",command=lambda :n("("),bg="orange",height="1",width="5").place(x=140,y=100)
c2 = Button(t,text=")",command=lambda :n(")"),bg="orange",height="1",width="5").place(x=140,y=130)
natija = Button(t,text="=",command=r,bg="green",height="1",width="5").place(x=140,y=160)
num7 = Button(t,text="7",command=lambda :n("7"),bg="white",height="1",width="4").place(x=5,y=70)
num8 = Button(t,text="8",command=lambda :n("8"),bg="white",height="1",width="4").place(x=50,y=70)
num9 = Button(t,text="9",command=lambda :n("9"),bg="white",height="1",width="4").place(x=95,y=70)
num4 = Button(t,text="4",command=lambda :n("4"),bg="white",height="1",width="4").place(x=5,y=100)
num5 = Button(t,text="5",command=lambda :n("5"),bg="white",height="1",width="4").place(x=50,y=100)
num6 = Button(t,text="6",command=lambda :n("6"),bg="white",height="1",width="4").place(x=95,y=100)
num1 = Button(t,text="1",command=lambda :n("1"),bg="white",height="1",width="4").place(x=5,y=130)
num2 = Button(t,text="2",command=lambda :n("2"),bg="white",height="1",width="4").place(x=50,y=130)
num3 = Button(t,text="3",command=lambda :n("3"),bg="white",height="1",width="4").place(x=95,y=130)
num0 = Button(t,text="0",command=lambda :n("0"),bg="white",height="1",bd=1,width="11").place(x=5,y=160)
num3 = Button(t,text=".",command=lambda :n("."),bg="white",height="1",width="4").place(x=95,y=160)
eff = Button(t,text="<<<",command=ed,bg="yellow",padx=2,height="1",width="4").place(x=145,y=35)
b1 = Button(t,text="sin",command=lambda :n("sin("),bg="white",height="1",width="4").place(x=5,y=195)
b2 = Button(t,text="e",command=lambda :n("e"),bg="white",height="1",width="4").place(x=50,y=195)
b3 = Button(t,text="π",command=lambda :n("π"),bg="white",height="1",width="4").place(x=95,y=195)
b4 = Button(t,text="cos",command=lambda :n("cos("),bg="white",height="1",width="4").place(x=5,y=225)
b5 = Button(t,text="tin",command=lambda :n("tin("),bg="white",height="1",width="4").place(x=50,y=225)
b6 = Button(t,text="asin",command=lambda :n("asin("),bg="white",height="1",width="4").place(x=95,y=225)
b7 = Button(t,text="atin",command=lambda :n("atin("),bg="white",height="1",width="4").place(x=5,y=255)
b8 = Button(t,text="acos",command=lambda :n("acos("),bg="white",height="1",width="4").place(x=50,y=255)
b9 = Button(t,text="log",command=lambda :n("log("),bg="white",height="1",width="4").place(x=95,y=255)
b10 = Button(t,text="log10",command=lambda :n("log10("),bg="white",height="1",width="4").place(x=5,y=285)
b11 = Button(t,text="log2",command=lambda :n("log2("),bg="white",height="1",width="4").place(x=50,y=285)
b12 = Button(t,text="√",command=lambda :n("sqrt("),bg="white",height="1",width="4").place(x=95,y=285)
b13 = Button(t,text="round",command=lambda :n("round("),bg="white",height="1",width="4").place(x=5,y=315)
b14 = Button(t,text=",",command=lambda :n(","),bg="white",height="1",width="4").place(x=50,y=315)
b15 = Button(t,text="tin",command=lambda :n("tin("),bg="white",height="1",width="4").place(x=95,y=315)
b16 = Button(t,text="atin",command=lambda :n("atin("),bg="white",height="1",width="5").place(x=140,y=195)
b17 = Button(t,text="sinh",command=lambda :n("sinh("),bg="white",height="1",width="5").place(x=140,y=225)
b18 = Button(t,text="asinh",command=lambda :n("asinh("),bg="white",height="1",width="5").place(x=140,y=285)
b19 = Button(t,text="acosh",command=lambda :n("acosh("),bg="white",height="1",width="5").place(x=140,y=315)
b20 = Button(t,text="cosh",command=lambda :n("cosh("),bg="white",height="1",width="5").place(x=140,y=255)
# from simple to scientifique
my_menu = Menu(t)
t.configure(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="نوع الآلة الحاسبة",menu=file_menu)
file_menu.add_command(label="الآلة الحاسبة العلمية",command=devl)
file_menu.add_separator()
file_menu.add_command(label="الآلة الحاسبة العادية",command=bat)
def key(event) :
    char = event.char
    if char in ['0','1','2','3','4','5','6','7','8','9','(',')','.','-','+','/','*'] :
       n(char)   
    elif char == "\r":
        r()
    elif char == "\x08":
        ed()
    elif char == "c":
        c()
t.bind("<Key>", key)
t.mainloop()