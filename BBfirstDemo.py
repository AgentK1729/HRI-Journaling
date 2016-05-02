import create
import dance
from time import sleep

r =create.Create('/dev/ttyUSB0')
#r.reset()
sleep(2)

print(r.getSensor('ANGLE'))
print(r.getSensor('DISTANCE'))

r.ser.flush()

print("first way")
r.go(0,25)
sleep(8)
print("other way!")
r.go(0,-25)
sleep(8)
r.shutdown()
