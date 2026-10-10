import csv
from tkinter import*
from datetime import datetime

win = Tk()
win.geometry('600x600')
win.title('message board')
win.resizable(0,0)

msglog = Label(win)

def logMsg(data: list):
    logs = ''
    for row in data:
        logs += f'{row[2]} | {row[0]}: {row[1]}\n'
    msglog.config(text=logs)

def sent():
    sentName = name.get()
    sentMessage = mesg.get()
    if not sentName.strip() or not sentMessage.strip():
        return
    time = str(datetime.now())[:-7]
    logged = [sentName,sentMessage,time]

    with open('msglogs.csv', 'r') as fl:
        reader = csv.reader(fl)
        data = list(reader)
    data.append(logged)

    with open('msglogs.csv', 'w', newline='') as fl:
        writer = csv.writer(fl)
        writer.writerows(data)

    logMsg(data)

with open('msglogs.csv', 'r') as fl:
    reader = csv.reader(fl)
    logMsg(reader)

name = Entry(win,font=('Arial',16,'bold'))
mesg = Entry(win,font=('Arial',16),width=40)
lab1 = Label(win,text='enter name:',font=('Arial',16,'bold'))
lab2 = Label(win,text='enter message:',font=('Arial',16,'bold'))
send = Button(win,text='send',font=('verdana',36,'bold'),command=sent)

lab1.pack();name.pack();lab2.pack();mesg.pack();send.pack();msglog.pack()

win.mainloop()

# note that the dates of the first 3 messages were obviously modified for placeholder reasons
# and also i made this like a long time ago, while we were learning tkinter