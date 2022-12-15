from machine import Pin
import time
import random

led = Pin(25, Pin.OUT)
timeout = time.time() + 150
while True:
    led.value(1)
    time.sleep(random.randrange(3))
    led.value(0)
    time.sleep(random.randrange(3))
    if time.time() > timeout:
        break
