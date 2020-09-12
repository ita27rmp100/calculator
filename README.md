# calculator
from tkinter import *
t = Tk()
t.title("الآلةالحاسبة")
t.geometry("190x280")
t.resizable(0,0)
t.configure(bg="black")
r = StringVar()

class calculation :
    def n1() :
        r.set(r.get()+"1")
    def n2() :
        r.set(r.get()+"2")
    def n3() :
        r.set(r.get()+"3")
    def n4() :
        r.set(r.get()+"4")
    def n5() :
        r.set(r.get()+"5")
    def n6() :
        r.set(r.get()+"6")
    def n7() :
        r.set(r.get()+"7")
    def n8() :
        r.set(r.get()+"8")
    def n9() :
        r.set(r.get()+"9")
    def n0() :
        r.set(r.get()+"0")
    def p() :
        r.set(r.get()+".")
    def r() :
        u = eval(r.get())
        r.set(u)            
    def c() :
        r.set("")
    def ope_ap() :
        r.set(r.get()+"+")
    def ope_f() :
        r.set(r.get()+"*")
    def ope_k() :
        r.set(r.get()+"/")
    def ope_p() :
        r.set(r.get()+"-")
    def ed() :
        bn = len(r.get())
        x = r.get()
        n = ""
        for i in range(0,bn-1) :
            n = n + str(x[i])
        r.set(str(n))
                 

amalia = Label(t,textvariable=r,font=("impact",15),width="18",height="0",bg="lightblue",fg="white").place(x=2,y=1)
kisma = Button(t,text="/",command=calculation.ope_k,bg="orange",height="1",width="3").place(x=5,y=35)
tharb = Button(t,text="*",command=calculation.ope_f,bg="orange",height="1",width="3").place(x=40,y=35)
nakis = Button(t,text="-",command=calculation.ope_p,bg="orange",height="1",width="3").place(x=75,y=35)
zaaid = Button(t,text="+",command=calculation.ope_ap,bg="orange",height="1",width="3").place(x=110,y=35)
clear = Button(t,text="C",command=calculation.c,bg="orange",height="1",width="5").place(x=140,y=85)
natija = Button(t,text="=",command=calculation.r,bg="orange",height="5",width="5").place(x=140,y=140)
num7 = Button(t,text="7",command=calculation.n7,bg="white",height="1",width="4").place(x=5,y=80)
num8 = Button(t,text="8",command=calculation.n8,bg="white",height="1",width="4").place(x=50,y=80)
num9 = Button(t,text="9",command=calculation.n9,bg="white",height="1",width="4").place(x=95,y=80)
num4 = Button(t,text="4",command=calculation.n4,bg="white",height="1",width="4").place(x=5,y=130)
num5 = Button(t,text="5",command=calculation.n5,bg="white",height="1",width="4").place(x=50,y=130)
num6 = Button(t,text="6",command=calculation.n6,bg="white",height="1",width="4").place(x=95,y=130)
num1 = Button(t,text="1",command=calculation.n1,bg="white",height="1",width="4").place(x=5,y=180)
num2 = Button(t,text="2",command=calculation.n2,bg="white",height="1",width="4").place(x=50,y=180)
num3 = Button(t,text="3",command=calculation.n3,bg="white",height="1",width="4").place(x=95,y=180)
num0 = Button(t,text="0",command=calculation.n0,bg="white",height="1",width="10").place(x=5,y=230)
num3 = Button(t,text=".",command=calculation.p,bg="white",height="1",width="4").place(x=95,y=230)
eff = Button(t,text="<<<",command=calculation.ed,bg="white",height="1",width="4").place(x=145,y=35)
t.mainloop()
