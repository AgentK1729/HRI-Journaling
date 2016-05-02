def initRobot():
        #This opens the serial connection to the create
        #if this raises an error, try /dev/ttyUSB1
        #if this is still an error try listing the ports in /dev/
        r =create.Create('/dev/ttyUSB0')
        #r.reset()
        sleep(2)

        #this is how you'd test sensors if you wanted
        #print(r.getSensor('ANGLE'))
        #print(r.getSensor('DISTANCE'))

        #this makes the input work by flushing the buffer
        r.ser.flush()

        #return the robot object to be used for turning
        return r

def turnToUser():
        r = initRobot()
        print("first way")
        r.go(0,25)
        sleep(8)
        r.go(0,0)

def turnFromUser():
        r = initRobot()
        print("other way!")
        r.go(0,-25)
        sleep(8)

        #this is to make sure it powers down
        r.shutdown()
