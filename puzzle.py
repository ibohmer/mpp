import machine
import utime
from utime import sleep
from machine import Pin

# Set pin 25 to output for LED
led = machine.Pin(25, Pin.OUT)
pin1 = machine.Pin(6, Pin.IN, Pin.PULL_DOWN)
pin2 = machine.Pin(9, Pin.IN, Pin.PULL_DOWN)
pin3 = machine.Pin(2, Pin.IN, Pin.PULL_DOWN)

# Define a blinking pattern of the dots and dashes of morse code
def dot():
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)
    
def dash():
    led.on()
    sleep(0.3)
    led.off()
    sleep(0.1)
  
# Define a function that will blink the solved state pattern without using sleep
def solvedBlink():
    while True:
        start = utime.ticks_ms()
        counter = start
        led.on()
        if counter = start + 100:
            led.off()
        if counter = start + 200:
            continue
        
# Initiliaze state variable
state = 1

# Start while loops to define behaviour in each state
while state = 1:
    startTime = utime.ticks_ms()
    counter = startTime
    
    # Blink to indicate state 1
    while counter < startTime + 3000:
        led.on()
        sleep(0.1)
        led.off()
        counter = utime.ticks_ms()
    
    # Blink morse code message "pin 6 high"
    while counter > startTime + 3000 and counter < starTime + 10000:
        # Pin
        dot()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        # 6
        dash()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        # High
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        
        sleep(2)
        
    if counter >= startTime + 10000:
        startTime = utime.ticks_ms()
        counter = startTime
        
    if pin1.value(1):
        state = 2
        
while state = 2:
    startTime = utime.ticks_ms()
    counter = startTime
    
    # Blink to indicate state 2
    while counter < startTime + 3000:
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
        led.on()
        sleep(0.1)
        led.off()
        counter = utime.ticks_ms()
    
    # Blink morse code message "pin 9 high"
    while counter > startTime + 3000 and counter < starTime + 10000:
        # Pin
        dot()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        # 9
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.5)
        
        # High
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        
        sleep(2)
        
    if counter >= startTime + 10000:
        startTime = utime.ticks_ms()
        counter = startTime
        
    if pin2.value(1):
        state = 3


 while state = 3:
    startTime = utime.ticks_ms()
    counter = startTime
    
    # Blink to indicate state 3
    while counter < startTime + 5000:
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
        led.on()
        sleep(0.1)
        led.off()
        counter = utime.ticks_ms()
    
    # Blink morse code message "pin 2 high"
    while counter > startTime + 5000 and counter < starTime + 10000:
        # Pin
        dot()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        # 2
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dash()
        sleep(0.5)
        
        # High
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dash()
        sleep(0.1)
        dash()
        sleep(0.1)
        dot()
        sleep(0.5)
        
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        sleep(0.1)
        dot()
        
        sleep(2)
        
    if counter >= startTime + 10000:
        startTime = utime.ticks_ms()
        counter = startTime
        
    if pin3.value(1):
        state = 4       
        
while state = 4:
    solvedBlink()
    print("PUZZLE SOLVED! Secret key: ce367ca99ebbbad16f9342f6c104e41a8f9b36b86cb11cef1b642f7ffac8893d")
        
        
        