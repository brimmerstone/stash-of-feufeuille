from tkinter import*
from tkinter import messagebox

win = Tk()
win.title('calculator')
win.geometry('400x450')
win.resizable(0,0)
a=2

display = ''
operations = ['+','-','*','/']

def calcInput(n):
    global display
    display += n
    lab.config(text=display)

def clear():
    global display
    display = ''
    lab.config(text=display)

def equal():
    global display, operations
    legal=True
    hasOperator = False
    display = str(display)
    if display == '' or display[-1] in operations:
        legal = False
    if legal:
        for i in display[1:]:
            if i in operations:
                hasOperator = True
                a,b = map(float,display.split(i))
                if i == '+':
                    display = a+b
                if i == '-':
                    display = a-b
                if i == '*':
                    display = a*b
                if i == '/':
                    if b==0:
                        legal = False
                        display = ''
                        lab.config(text=display)
                        messagebox.showerror('Warning',"You can't divide by 0")
                    else:
                        display = a/b
                if display.is_integer():
                    display = int(display)
                else:
                    display = round(display,13-len(str(int(display))))
                break
    if not hasOperator:
        legal = False
    if legal:
        display = str(display)
        lab.config(text=display)

def operation(sign):
    global display,operations
    legal = True
    allow = True
    if display == '':
        if sign != '-':
            allow = False
    else:
        display = str(display)
        if display[-1] in operations:
            display = display[:-1]
        hasOperator = False
        for i in display[1:]:
            if i in operations:
                a, b = map(float, display.split(i))
                if i == '+':
                    display = a+b
                if i == '-':
                    display = a-b
                if i == '*':
                    display = a*b
                if i == '/':
                    if b == 0:
                        legal = False
                        display = ''
                        lab.config(text=display)
                        messagebox.showerror('Warning', "You can't divide by 0")
                    else:
                        display = a / b
                if display.is_integer():
                    display = int(display)
                else:
                    display = round(display,13-len(str(int(display))))
                break
        if not hasOperator:
            legal = False
        if legal:
            display = str(display)
            lab.config(text=display)

    if allow:
        display = str(display) + sign
        lab.config(text=display)

def pointInput():
    global display,operations
    legal = True; hasOperations = False
    for i in display:
        if i in operations:
            hasOperations = True
            a, b = map(str, display.split(i))
            for i in b:
                if i == '.':
                    legal=False
    if not hasOperations:
        for i in display:
            if i == '.':
                legal=False
    if legal:
        display += '.'
        lab.config(text=display)

def mode(theme):
    if theme == 'dark':
        win.config(bg='#303030'); fill.config(bg='#303030')
        lab.config(bg='black',fg='silver')
        n0.config(bg='gray', activebackground='#303030',activeforeground='white')
        n1.config(bg='gray', activebackground='#303030',activeforeground='white')
        n2.config(bg='gray', activebackground='#303030',activeforeground='white')
        n3.config(bg='gray', activebackground='#303030',activeforeground='white')
        n4.config(bg='gray', activebackground='#303030',activeforeground='white')
        n5.config(bg='gray', activebackground='#303030',activeforeground='white')
        n6.config(bg='gray', activebackground='#303030',activeforeground='white')
        n7.config(bg='gray', activebackground='#303030',activeforeground='white')
        n8.config(bg='gray', activebackground='#303030',activeforeground='white')
        n9.config(bg='gray', activebackground='#303030',activeforeground='white')
        n00.config(bg='gray',activebackground='#303030',activeforeground='white')
        clear.config(bg='#A08000',activebackground='#303030',activeforeground='white')
        equal.config(bg='#C08000',activebackground='#303030',activeforeground='white')
        plus.config(bg='teal', activebackground='#303030',activeforeground='white')
        minus.config(bg='teal',activebackground='#303030',activeforeground='white')
        mult.config(bg='teal', activebackground='#303030',activeforeground='white')
        div.config(bg='teal',  activebackground='#303030',activeforeground='white')
        point.config(bg='#806000',activebackground='#303030',activeforeground='white')
        dark.place_forget()
        light.place(x=0, y=450, anchor='sw')
    if theme == 'light':
        win.config(bg='white'); fill.config(bg='white')
        lab.config(bg='silver',fg='black')
        n0.config(bg='silver',activebackground='white', activeforeground='black')
        n1.config(bg='silver',activebackground='white', activeforeground='black')
        n2.config(bg='silver',activebackground='white', activeforeground='black')
        n3.config(bg='silver',activebackground='white', activeforeground='black')
        n4.config(bg='silver',activebackground='white', activeforeground='black')
        n5.config(bg='silver',activebackground='white', activeforeground='black')
        n6.config(bg='silver',activebackground='white', activeforeground='black')
        n7.config(bg='silver',activebackground='white', activeforeground='black')
        n8.config(bg='silver',activebackground='white', activeforeground='black')
        n9.config(bg='silver',activebackground='white', activeforeground='black')
        n00.config(bg='silver',activebackground='white',activeforeground='black')
        clear.config(bg='gold',activebackground='white',activeforeground='black')
        equal.config(bg='orange',activebackground='white', activeforeground='black')
        plus.config(bg='#189BCC',activebackground='white', activeforeground='black')
        minus.config(bg='#189BCC',activebackground='white',activeforeground='black')
        mult.config(bg='#189BCC',activebackground='white', activeforeground='black')
        div.config(bg='#189BCC',activebackground='white',  activeforeground='black')
        point.config(bg='tan',activebackground='white',    activeforeground='black')
        light.place_forget()
        dark.place(x=0, y=450, anchor='sw')

lab = Label(bg='silver',width=15,height=1,bd=5,relief=SUNKEN,font=('lucida console',24,'bold'),anchor=E)
n0 = Button(text='0',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('0'))
n1 = Button(text='1',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('1'))
n2 = Button(text='2',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('2'))
n3 = Button(text='3',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('3'))
n4 = Button(text='4',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('4'))
n5 = Button(text='5',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('5'))
n6 = Button(text='6',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('6'))
n7 = Button(text='7',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('7'))
n8 = Button(text='8',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('8'))
n9 = Button(text='9',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('9'))
n00 =Button(text='00',width=a*2,height=a,font=('Verdana',14,'bold'),bg='silver',command=lambda: calcInput('00'))
plus  = Button(text='+',width=a*2,height=a,font=('Verdana',14,'bold'),bg='#189BCC',command=lambda: operation('+'))
minus = Button(text='-',width=a*2,height=a,font=('Verdana',14,'bold'),bg='#189BCC',command=lambda: operation('-'))
mult  = Button(text='*',width=a*2,height=a,font=('Verdana',14,'bold'),bg='#189BCC',command=lambda: operation('*'))
div   = Button(text='/',width=a*2,height=a,font=('Verdana',14,'bold'),bg='#189BCC',command=lambda: operation('/'))
point = Button(text='.',width=a*2,height=a,font=('Verdana',14,'bold'),bg='tan',command=pointInput)
equal = Button(text='=',width=a*2,height=a,font=('Verdana',14,'bold'),bg='orange',command=equal)
clear = Button(text='C',width=a*2,height=a,font=('Verdana',14,'bold'),bg='gold',command=clear)

dark =  Button(text='dark mode' ,bg='gray', font=('Verdana',14),command=lambda: mode('dark'))
light = Button(text='light mode',bg='silver',font=('Verdana',14),command=lambda: mode('light'))
fill = Label(font=('Calibri',4))

fill.pack(); lab.pack()
n0.place(x=55, y=300); n1.place(x=55, y=225)
n2.place(x=130,y=225); n3.place(x=205,y=225)
n4.place(x=55, y=150); n5.place(x=130,y=150)
n6.place(x=205,y=150); n7.place(x=55, y=75)
n8.place(x=130,y=75); n9.place(x=205, y=75)
n00.place(x=130,y=300)

clear.place(x=205,y=375); equal.place(x=205,y=300)
plus.place(x=280, y=300); minus.place(x=280,y=225)
mult.place(x=280, y=150); div.place(x=280,y=75)
point.place(x=130,y=375)

dark.place(x=0,y=450,anchor='sw')

win.mainloop()
