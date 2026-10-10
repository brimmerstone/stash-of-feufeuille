from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox

win = Tk()
win.title('Morse Code Translator')
win.geometry('500x500')
win.resizable(0,0)

font = 'Lucida Console'
set = ''
dict = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..',
        'J':'-...','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
        'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
        '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
        '8':'---..','9':'----.','0':'-----','?':'--..--','!':'-.-.--','.':'.-.-.-',",":"--..--",
        ';':'-.-.-.',':':'---...','+':'.-.-.','-':'-....-','/':'-..-.','=':'-...-',' ':'/'}

def pick():
    global set
    set = box.get()
    if set == 'Text to Morse Code':
        lb1.place(x=250,y=100,anchor=CENTER)
        en1.place(x=250,y=125,anchor=CENTER)
    else:
        lb2.place(x=250,y=100,anchor=CENTER)
        en2.place(x=250,y=125,anchor=CENTER)
    trans.place(x=250,y=150,anchor=CENTER)
    result.place(x=250,y=175,anchor=CENTER)

def translate():
    global set,dict
    txt = ''
    if set == 'Text to Morse Code':
        vars = [var for var in en1.get().upper()]
        for i in vars:
            if i in dict:
                txt += dict[i] + ' '
    if set == 'Morse Code to Text':
        vars = en2.get().replace('_','-').split()
        for i in vars:
            for let,v in dict.items():
                if i == v:
                    txt += let.upper()
    result.config(text=txt)

def info():
    messagebox.showinfo('Help',"Use - or _ symbols for long beeps, and use . for short beeps."
        "\nMake sure to separate your letters via space and separate your words by using the / symbol alongside spaces.")

legend = Label(win, text='Morse Code Translator',font=(font,20,'bold'))
box = Combobox(win,font=(font,10))
box['values'] = ('Text to Morse Code','Morse Code to Text')
box.current(0)
clk = Button(win,text='Choose',font=(font,10),command=pick)

lb1 = Label(win,text='Text to Morse Code',font=(font,12))
en1 = Entry(win,font=(font,12))
lb2 = Label(win,text='Morse Code to Text',font=(font,12))
en2 = Entry(win,font=(font,12))
trans = Button(win,text='Translate',font=(font,12),command=translate)
result = Label(win,text='',font=(font,12))

help = Button(win,text='Help',font=(font,14),bg='silver',command=info)

legend.place(x=250,y=15,anchor=N)
box.place(x=185,y=60,anchor=CENTER)
clk.place(x=315,y=60,anchor=CENTER)
help.place(x=0,y=500,anchor=SW)
result.place(x=250,y=250,anchor=CENTER)

win.mainloop()
