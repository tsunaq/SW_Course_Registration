import time
import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from pynput import mouse
import pyautogui


root = Tk()
root.title('수강신청')
root.geometry('410x175+100+100')

##

global bunban
global gwamok
global numofpeople

##
entry1 = Entry(root, width=10)
entry1.grid(row=1, column=1)

entry2 = Entry(root, width=10)
entry2.grid(row=1, column=2)

button1 = Button(root, text="마우스 좌표 설정", command=lambda:aaa())
button1.grid(row=1, column=3)

subject = StringVar()
entry3 = Entry(root, width=10, textvariable=subject)
entry3.grid(row=2, column=1)

button2 = Button(root, text='과목코드 설정', command=lambda:ddd())
button2.grid(row=2, column=2)


bunban = StringVar()
entry4 = Entry(root, width=10, textvariable=bunban)
entry4.grid(row=3, column=1)

button3 = Button(root, text='    분반 설정    ', command=lambda:eee())
button3.grid(row=3, column=2)

numofpeople = StringVar()
entry5 = Entry(root, width=10, textvariable=numofpeople)
entry5.grid(row=4, column=1)

button4 = Button(root, text='수강정원 설정', command=lambda:ggg())
button4.grid(row=4, column=2)

button5 = Button(root, text='시작', command=lambda:fff())
button5.grid(row=5, column=3)

button6 = Button(root, text='중지')
button6.grid(row=5, column=4)

##


def aaa():
    with mouse.Listener(
        on_click=bbb
    ) as listener:
        listener.join()
    ccc()


def bbb(x, y, button, pressed):
    if pressed:
        global x1
        global y1
        x1 = x
        y1 = y

    if not pressed:
        return False


def ccc():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry1.insert('end', x1)
    entry2.insert(0, y1)


def ddd():
    global gwamok
    gwamok = Entry.get(entry3)
    print(gwamok)


def eee():
    global bunban
    bunban = Entry.get(entry4)
    print(bunban)


def fff():
    thread_run()


def ggg():
    global bunban
    bunban = Entry.get(entry5)
    print(bunban)


def thread_run():
    global x1
    global y1
    global bunban
    global numofpeople

    xxx = "########비공개링크########" + gwamok
    html = urlopen(xxx)
    bsObject = BeautifulSoup(html, "html.parser")

    print('=====', time.ctime(), '=====')

    a = []
    b = []

    result = bsObject.select('####비공개####')
    number = bsObject.select('####비공개####')

    for r in result:
        a.append(r.text)

    for r in number:
        b.append(r.text)

    index = int(bunban) - 1

    if a[index] != b[index]:
        pyautogui.click(x1, y1)

    th = threading.Timer(1, thread_run)

    th.start()


root.mainloop()