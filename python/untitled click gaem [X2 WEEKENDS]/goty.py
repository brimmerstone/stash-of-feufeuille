from tkinter import*
from random import randint,choice

wid=600;hei=600;edge=80

win = Tk()
win.resizable(0,0)
win.geometry(f"{wid}x{hei}")
win.title('button simulator')

font = 'Comic Sans MS'
score = 0
fakenames = ['wrong button','click me','click me to pass','im real trust','click for robux',
             'EVIL button','true buttom','ture button','not anomaly button','normal button',
             'THE real button','real buton','reel button','realbutton','real button','real button',
             'real button','REAL BUTTON','reol button','real button','real button','real button',
             'real button','real button','click me dummy','a real button','imposter button','sus button']

colors = ['#A0A0A0','gray','black','red','orange','gold','purple','#189BCC','blue','#00C0FF','teal']

def fakespawn():
    global fakenames,colors,wid,hei,edge,realCol
    name = choice(fakenames)
    col = choice(colors)
    if name == 'real button':
        fake.config(text=name,bg=col,activebackground='white',activeforeground='red')
    elif name == 'EVIL button' or name == 'imposter button' or name == 'sus button':
        fake.config(text=name,bg='red',activebackground='white',activeforeground='black')
    else:
        fake.config(text=name,bg=col,activebackground='white',activeforeground='black')

    fake.place(x=randint(0+edge,wid-edge),y=randint(0+edge*2,hei-edge),anchor=CENTER)

def set():
    global score,hs,wid,hei,edge,realCol,colors,start
    if score > hs:
        hs = score
    stats.config(text=f'Score: {score} / Highscore: {hs}')
    fake.place_forget()
    realCol = choice(colors)
    real.config(bg=realCol)
    real.place(x=randint(0+edge,wid-edge),y=randint(0+edge*2,hei-edge),anchor=CENTER)
    if start:
        fakespawn()

def click():
    global score,fnc,start
    score+=1
    start=True
    set()
    if fnc:
        win.after_cancel(fnc)
    fnc = win.after(3000,set)

def faked():
    global wid,hei,score
    real.place_forget()
    fake.place_forget()
    lose.place(x=wid//2,y=hei//2,anchor=CENTER)
    with open('highscore.txt', 'r') as fl:
        hs = fl.read()
        if score > int(hs):
            with open('highscore.txt', 'w') as fl:
                fl.write(str(score))

with open('highscore.txt', 'r') as fl:
    hs = fl.read()
    hs = int(hs)
title = Label(text='button simulator',font=(font,16))
title.place(x=wid//2,y=0,anchor=N)
stats = Label(text=f'Score: {score} / Highscore: {hs}',font=(font,16))
stats.place(x=wid//2,y=30,anchor=N)

start = False
fake = Button(font=(font,16),bg='teal',fg='white',command=faked)
lose = Label(text='you lost silly billy',font=(font,50))

realCol = choice(colors)
real = Button(text='real button',font=(font,16),fg='white',bg=realCol,command=click)
real.place(x=randint(0+edge,wid-edge),y=randint(0+round(edge*1.5),hei-edge),anchor=CENTER)
fnc = win.after(3000,set)

# def testcmd():
#     click()
#     win.after(100,testcmd)
# testcmd()

win.mainloop()