from os import system
from time import sleep
from Tkinter import *
from tkFont import Font
import threading, vlc
from tts import speak


class AlertThread(threading.Thread):
	def __init__(self, proc):
		threading.Thread.__init__(self)
		self.proc = proc
		
	def run(self):
		if self.proc == 0:
			alert = Tk()
			Label(alert, text=" ", font=Font(size=50)).grid(row=0, column=0)
			Label(alert, text=" ", font=Font(size=50)).grid(row=0, column=1)
			Label(alert, text=" ", font=Font(size=50)).grid(row=1, column=0)
			Label(alert, text="Please make a journal entry", font=Font(size=50)).grid(row=1, column=1)
			Label(alert, text=" ", font=Font(size=50)).grid(row=2, column=0)
			Label(alert, text=" ", font=Font(size=50)).grid(row=2, column=1)
			Label(alert, text=" ", font=Font(size=50)).grid(row=2, column=2)
			alert.mainloop()
			
		elif self.proc == 1:
			vlc.MediaPlayer('alert.mp3').play()
			
		elif self.proc == 3:
			speak()
			
		else:
			import screen1
			screen1.top.mainloop()
		



while True:
	threads = [AlertThread(2), AlertThread(0), AlertThread(1), AlertThread(3)]
	threads[0].start()
	threads[3].start()
	sleep(7200)
	threads[1].start()
	threads[2].start()
