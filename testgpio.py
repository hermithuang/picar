#!/usr/bin/python
#light
import RPi.GPIO as GPIO
import time
 
port = 11
print GPIO.OUT
print GPIO.HIGH
GPIO.setmode(GPIO.BOARD)
GPIO.setup(port, GPIO.OUT)
 
try:
#  while True:
#    GPIO.output(12, GPIO.HIGH) 
#    time.sleep(1)
#    GPIO.output(12, GPIO.LOW)
#    time.sleep(1)
  GPIO.output(port, GPIO.HIGH) 
  time.sleep(5)
  GPIO.output(port, GPIO.LOW)
  time.sleep(20)
except KeyboardInterrupt:
  GPIO.cleanup()
  print "All Cleanup!"
