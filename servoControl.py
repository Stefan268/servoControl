import RPi.GPIO as GPIO
import GPIO.PWM as PWM
import time
from lidar_lite import Lidar_Lite

global distances[]

connected = (-1)
lidar = Lidar_Lite()
while (connected == -1):
    connected = lidar.connect(1)

def getDist(self):
    return self.lidar.getDistance()

def setup(resolution):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    
    servo = PWM(18, 50)
    servo.start(0)
    
def sweepRight():
        for duty in range(11):
            servo.ChangeDutyCycle(duty * 10)
            time.sleep(1)#pause and wait for movement
            distances[duty] = getDist()
        return distances
def sweepLeft():        
        for duty in range(10,-1,-1):
            servo.ChangeDutyCycle(duty * 10)
            time.sleep(1)#pause and wait for movement
            distances[duty] = getDist()
        return distances
