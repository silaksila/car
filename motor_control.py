import time
import gpiozero

wheels = gpiozero.Robot(left=(25, 8), right=(7, 1))

wheels.forward()
time.sleep(3)
wheels.right()
time.sleep(3)
wheels.left(3)
time.sleep(3)
wheels.stop()
