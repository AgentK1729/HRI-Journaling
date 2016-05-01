import pyttsx

def speak():
	engine = pyttsx.init()
	engine.say("hello!")
	engine.say("how")
	engine.say("are")
	engine.say("you")
	engine.say("feeling")
	engine.say("today?")
	engine.runAndWait()	
