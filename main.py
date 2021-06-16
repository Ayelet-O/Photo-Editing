import cv2
from tkinter import *
import random
from picture import Picture
class MyImg:
    x_start, y_start, x_end, y_end = -500, -500, -500, -500
    event=""
    def __init__(self,win):
        self.img = Picture("image")
        self.txt1 = Entry(win)
        self.txt2 = Entry(win)
        self.lbl1 = Label(win, text='Photo editing',bg='#FFE4E1', font=('David', 30))
        self.btn1 = Button(win, text='choose a picture',height=3, width=50,bg='#EEA2AD')
        self.lbl2 = Label(win, text='Editing Functions',bg='#FFE4E1', font=('David', 20))
        self.btn2 = Button(win, text='cut the picture',height=2,bg='#EEA2AD')
        self.btn3 = Button(win, text='add text to the picture',bg='#EEA2AD',height=2, width=18,command=lambda:self.img.addText(self.txt1))
        self.btn4 = Button(win, text='add rectangle to the picture',bg='#EEA2AD',height=2, width=23)
        self.btn5 = Button(win, text='add circle to the picture',bg='#EEA2AD',height=2)
        self.lbl3 = Label(win, text='enter the text to add to the image',bg='#FFE4E1', font=('David', 12))
        self.btn6 = Button(win, text='save changes',bg='#EEA2AD',height=1, width=50,command=lambda:self.img.savingImg(self.txt2))
        self.lbl4 = Label(win, text='enter the name of the new image',bg='#FFE4E1', font=('David', 12))
        self.btn7 = Button(win, text='exit',bg='#EEA2AD', command=win.destroy)
        self.btn8 = Button(win, text='blur image',bg='#EEA2AD',height=2)
        self.positions()
        self.events()
    def positions(self):
        self.btn1.place(x=150,y=50)
        self.btn2.place(x=350,y=270)
        self.btn3.place(x=150, y=270)
        self.btn4.place(x=350, y=190)
        self.btn5.place(x=150, y=190)
        self.btn6.place(x=150, y=420)
        self.btn7.place(x=560, y=470)
        self.btn8.place(x=450, y=270)
        self.lbl1.place(x=200,y=0)
        self.lbl2.place(x=200, y=130)
        self.lbl3.place(x=150, y=350)
        self.txt1.place(x=365,y=350)
        self.lbl4.place(x=150, y=390)
        self.txt2.place(x=365, y=390)
    def events(self):
        self.btn1.bind('<Button-1>', self.img.chooseImg)
        self.btn2.bind('<Button-1>', self.img.cutImgCV2)
        # self.btn3.bind('<Button-1>', self.img.addTextCV2)
        self.btn4.bind('<Button-1>', self.img.addShap)
        self.btn5.bind('<Button-1>', self.img.addShap2)
        # self.btn6.bind('<Button-1>', self.img.savingImg)
        self.btn8.bind('<Button-1>', self.img.blurImag)
# def changeBackgroundColor(event):
#     #color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
#     window['background']=color
window=Tk()
mywin=MyImg(window)
window.title=('my project')
window.geometry("600x500+600+300")
window.configure(bg='#FFE4E1')
window.mainloop()
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
