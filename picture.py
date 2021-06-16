import cv2
import numpy as np
from tkinter import filedialog as fd
import random
cropping = False
drawing =False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
x_text, y_text=0,0
class Picture:
    def __init__(self, nameWindow):
        self.__file_name = ""
        self.__nameWindow = nameWindow
        self.__img = ""
        self.win=""
        self.text = ""

    def setfilename(self, filename):
        self.__file_name = filename

    def getfilename(self):
        return self.__file_name

    file_name = property(getfilename, setfilename)

    def setnameWindow(self, nameWindow):
        self.__nameWindow = nameWindow

    def getnameWindow(self):
        return self.__nameWindow

    nameWindow = property(getnameWindow, setnameWindow)

    def setimg(self, img):
        self.__img = img

    def getimg(self):
        return self.__img

    img = property(getimg, setimg)

    def chooseImg(self,event):
        self.file_name = fd.askopenfilename(initialdir="C:\\Users\\user\\birds", title="choose a picture")
        self.img = cv2.imread(self.file_name)
        self.img = cv2.resize(self.img, (500, 500))
        cv2.imshow(self.nameWindow, self.img)
        cv2.setMouseCallback(self.nameWindow, self.randomColors)

    def cutImgCV2(self,event):
        cv2.setMouseCallback(self.nameWindow, self.cutImg)
    def cutImg(self,event, x, y, flags, param):
        global x_start, y_start, x_end, y_end, cropping
        if event == cv2.EVENT_LBUTTONDOWN:
            x_start, y_start, x_end, y_end = x, y, x, y
            cropping = True
        elif event == cv2.EVENT_MOUSEMOVE:
            if cropping == True:
                x_end, y_end = x, y
        elif event == cv2.EVENT_LBUTTONUP:
                x_end, y_end = x, y
                cropping = False
                refPoint = [(x_start, y_start), (x_end, y_end)]
                if len(refPoint) == 2:  # when two points were found
                    roi = self.img[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                    cv2.imshow("Cropped", roi)
        if event==cv2.EVENT_RBUTTONDOWN:
            cv2.setMouseCallback(self.nameWindow, self.randomColors)

    def check(self,event,x,y,flags,params):
        global x_text, y_text
        if event == cv2.EVENT_LBUTTONDOWN:
            x_text = x
            y_text = y
        if event==cv2.EVENT_RBUTTONDOWN:
            cv2.setMouseCallback(self.nameWindow, self.randomColors)
    def addText(self,text):
        cv2.setMouseCallback(self.nameWindow, self.check)
        self.text=str(text.get())
        cv2.putText(self.img, self.text, (x_text, y_text), cv2.FONT_HERSHEY_PLAIN, 3.5, (0, 0, 255), 4)
        cv2.imshow(self.nameWindow, self.img)

    def addShap(self,event):
        cv2.setMouseCallback(self.nameWindow, self.draw_rect)
    def draw_rect(self,event, x, y, flags, param):
        global x_start, y_start, x_end, y_end, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            x_start = x
            y_start = y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            x_end = x
            y_end = y
            cv2.rectangle(self.img, (x_start, y_start), (x_end, y_end), (0, 255, 0), 10)
            cv2.imshow(self.nameWindow, self.img)
        if event==cv2.EVENT_RBUTTONDOWN:
            cv2.setMouseCallback(self.nameWindow, self.randomColors)

    def addShap2(self,event):
        cv2.setMouseCallback(self.nameWindow, self.draw_circle)
    def draw_circle(self,event, x, y, flags, param):
        global x_start, y_start, x_end, y_end, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            x_start = x
            y_start = y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            x_end = x
            y_end = y
            cv2.circle(self.img, (x_start, y_start),x_end-x_start, (255, 0, 0), 10)
            cv2.imshow(self.nameWindow, self.img)
        if event==cv2.EVENT_RBUTTONDOWN:
            cv2.setMouseCallback(self.nameWindow, self.randomColors)

    def savingImg(self,text):
        self.text = str(text.get())
        cv2.imwrite(str(self.text)+'.jpg', self.img)

    def randomColors(self,event,x, y, flags, param):
        colors = [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_HSV2BGR, cv2.COLOR_RGB2BGR, cv2.COLOR_RGBA2RGB,
                  cv2.COLOR_BGR2HSV]
        if event == cv2.EVENT_RBUTTONDOWN:
            self.img = cv2.cvtColor(self.img, random.choice(colors))
            cv2.imshow(self.nameWindow, self.img)

    def blurImag(self,event):
        self.img=cv2.GaussianBlur(self.img, (5, 5), 0)
        cv2.imshow(self.nameWindow, self.img)