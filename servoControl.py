import RPi.GPIO as GPIO
import GPIO.PWM as PWM
import time
from lidar_lite import Lidar_Lite



class lidarControl:

    def setup(self, resolution):
        self.lidar = Lidar_Lite()
        self.lidar.connect(1)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        
        self.servo = PWM(18, 50)
        self.servo.start(0)
        self.resolution = resolution
        
    def sweepRight(self):
            for duty in range(self.resolution):
                self.servo.ChangeDutyCycle(duty * 100/(self.resolution - 1)
                time.sleep(1)#pause and wait for movement
                self.distances[duty] = self.lidar.getDistance()
            return distances
    def sweepLeft(self):        
            for duty in range((self.resolution-1),-1,-1):
                self.servo.ChangeDutyCycle(duty * 100/(self.resolution - 1))
                time.sleep(1)#pause and wait for movement
                self.distances[duty] = self.lidar.getDistance()
            return distances
