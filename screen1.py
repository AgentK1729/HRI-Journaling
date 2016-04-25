from Tkinter import *
import tkMessageBox
from tkFont import Font
from PIL import ImageTk, Image
import requests

def record():
	link = "https://api.thingspeak.com/update?api_key=WGMFL5ZJKPORH0IN&field1=%d&field2=%d&field3=%d&field4=%d&field5=%d&field6=%d&field7=%d"
	
	try:
		f1 = open("id.txt", "r")
		ID = int(f1.read())
	
	except IOError:
		from random import randint
		f1 = open("id.txt", "w")
		f1.write(str(randint(1,1000)))
		f1 = open("id.txt", "r")
		ID = int(f1.read())
	
	link = link % (ID, var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get())
	r = requests.get(link)
	
	link = "https://api.thingspeak.com/update?api_key=PDXN073A0L2GXWXF&field1=%s&field2=%s&field3=%s&field4=%s"
	link = link % (ID, day.get(1.0,END), accomplish.get(1.0,END), feeling.get(1.0,END))
	r = requests.get(link)
	
   

def sel():
   selection = str(var.get())
   label.config(text = selection)

top = Tk()


var1 = DoubleVar()
Label(top, text="Happy", font=Font(size=15)).grid(row=1, column=0)
happyImg = ImageTk.PhotoImage(Image.open("happy.png").resize((80,80), Image.ANTIALIAS))
happyPanel = Label(top, image=happyImg)
happyPanel.grid(row=0, column=0)
happyScale = Scale(top, variable=var1, orient="horizontal", from_=0, to=10).grid(row=2, column=0)

Label(top, text="Sad", font=Font(size=15)).grid(row=1, column=1)
var2 = DoubleVar()
sadImg = ImageTk.PhotoImage(Image.open("sad.png").resize((80,80), Image.ANTIALIAS))
sadPanel = Label(top, image=sadImg)
sadPanel.grid(row=0, column=1)
sadScale = Scale(top, variable=var2, orient="horizontal", from_=0, to=10).grid(row=2, column=1)

Label(top, text="Anxious", font=Font(size=15)).grid(row=1, column=2)
var3 = DoubleVar()
anxiousImg = ImageTk.PhotoImage(Image.open("anxious.png").resize((80,80), Image.ANTIALIAS))
anxiousPanel = Label(top, image=anxiousImg)
anxiousPanel.grid(row=0, column=2)
anxiousScale = Scale(top, variable=var3, orient="horizontal", from_=0, to=10).grid(row=2, column=2)



Label(top, text="Angry", font=Font(size=15)).grid(row=4, column=0)
var4 = DoubleVar()
angryImg = ImageTk.PhotoImage(Image.open("angry.png").resize((80,80), Image.ANTIALIAS))
angryPanel = Label(top, image=angryImg)
angryPanel.grid(row=3, column=0)
angryScale = Scale(top, variable=var4, orient="horizontal", from_=0, to=10).grid(row=5, column=0)

Label(top, text="Exhausted", font=Font(size=15)).grid(row=4, column=1)
var5 = DoubleVar()
exhaustedImg = ImageTk.PhotoImage(Image.open("exhausted.png").resize((80,80), Image.ANTIALIAS))
exhaustedPanel = Label(top, image=exhaustedImg)
exhaustedPanel.grid(row=3, column=1)
exhaustedScale = Scale(top, variable=var5, orient="horizontal", from_=0, to=10).grid(row=5, column=1)

Label(top, text="Excited", font=Font(size=15)).grid(row=4, column=2)
var6 = DoubleVar()
emptyImg = ImageTk.PhotoImage(Image.open("empty.png").resize((80,80), Image.ANTIALIAS))
emptyPanel = Label(top, image=emptyImg)
emptyPanel.grid(row=3, column=2)
emptyScale = Scale(top, variable=var6, orient="horizontal", from_=0, to=10).grid(row=5, column=2)


Label(top, text="    ", font=Font(size=15)).grid(row=1, column=3)
Label(top, text="    ", font=Font(size=15)).grid(row=1, column=4)
Label(top, text="    ", font=Font(size=15)).grid(row=1, column=5)

Label(top, text="Tell me about your day", font=Font(size=15)).grid(row=1, column=6)
day = Text(top, height=10)
day.grid(row=2, column=6)

Label(top, text="What did you accomplish today?", font=Font(size=15)).grid(row=4, column=6)
accomplish = Text(top, height=10)
accomplish.grid(row=5, column=6)

Label(top, text="How are you feeling?", font=Font(size=15)).grid(row=6, column=6)
feeling = Text(top, height=10)
feeling.grid(row=7, column=6)

Label(top, text="", font=Font(size=15)).grid(row=8, column=0)
Label(top, text="", font=Font(size=15)).grid(row=8, column=1)
Label(top, text="", font=Font(size=15)).grid(row=8, column=2)

Label(top, text="    ", font=Font(size=15)).grid(row=1, column=7)
Label(top, text="    ", font=Font(size=15)).grid(row=1, column=8)

B = Button(top, text ="Done", font=Font(size=15), command = record, height=3, width=20).grid(row=6, column=1)
