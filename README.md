# SW_Course_Registration

## 1. 설계목적
2019학년도 겨울방학기간을 통해 파이썬을 학습하고자 했고, 눈에 보이는 뚜렷한 작업물을 만들고 싶었는데 수강신청 기간이 겹쳐서 수강신청을 도울 수 있는 프로그램을 제작

## 2. 프로그램 설계에 이용한 라이브러리
1. 웹 크롤링을 위한 BeautifulSoup, urlopen
2. 쓰레딩 생성을 위한 time, threading
3. GUI를 위한 tkinter
4. 마우스 조작을 위한 pyautogui

## 3. 코드

thread_run 함수의 xxx 변수는 웹 크롤링을 하기 위한 url, result/number 변수는 크롤링에서 내가 필요한 정보들을 나타낸다.  
공개된 코드가 악용의 우려가 있기 때문에 xxx, result, number 변수에 들어갈 부분을 비공개 처리하였고, 평가가 완료된 후 본 리포지터리는 비공개 할 예정이다.

```python
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
```

## 4. 결과 및 고찰
단순히 파이썬을 학습하고, 눈에 띄는 작업물을 만들기 위해 수강신청 프로그램을 만들었으나 실제로 본 수강신청에서는 작성한 프로그램의 정상 작동 여부를 확인할 때 외에는 사용하지 않았다.  
결과적으로는 프로그램이 완성되었는데 이 프로그램은 웹 크롤링을 수행해서 원하는 정보를 추출해낼 수 있었다. 추출한 정보들이 조건문을 만족하지 못했을 때, pyautogui 라이브러리를 이용해 지정한 좌표에 위치한 수강신청 버튼을 클릭하는 행동을 수행했다.  

학부생의 지식으로도 웹 크롤링을 수행하고, 마우스와 키보드를 제어할 수 있는 수준의 프로그램을 만들 수 있다는 점은 매우 놀라웠다. 이렇듯 누구나 약간의 지식으로도 손쉽게 다룰 수 있다는 점은 파이썬 언어의 장점이지만, 한편으로는 악용의 소지도 존재한다. 학부생조차도 프로그래밍 언어를 통해 정교하게 작동하는 수강신청 매크로를 만들수 있기 때문에 다른 학우들에게 피해를 끼칠 수 있다. 실제로 에브리타임 등 대학 커뮤니티를 보면 수강신청 매크로 구매/판매글, 인기 강의에 대한 구매/판매글이 종종 존재한다.

현재 우리 학교의 수강신청 시스템은 사용자가 수강꾸러미에 담긴 과목의 수강신청 버튼을 500회 클릭했을 경우, 담아둔 수강꾸러미를 일괄 삭제하고 다시 수강신청을 하기 위해서 사용자에게 과목코드와 자동입력방지 문자의 입력을 요구한다.  
이와 같은 매크로 프로그램을 막기 위해서는 다음과 같은 조치가 필요하다.  
1. 수강꾸러미에 담아둔 과목의 신청 버튼 위치 랜덤화
2. 일정한 주기로 수업시간표, 수강신청 페이지에 접속하는 사용자 일시차단
3. 수강신청 페이지 새로고침 횟수 제한
4. 수강꾸러미 등록한 과목에 자동입력방지 문자 추가

  
