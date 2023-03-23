import board
from rpi_ws281x import *
import time
import random

LED_COUNT      = 100      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 1000000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0 

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()
def idle():
    red = random.randint(0,20)
    green = random.randint(0,20)
    blue = random.randint(0,20)
    unit = 200 / (red+green+blue)
    for i in range(red*int(unit)):
        for j in range(LED_COUNT):
            strip.setPixelColor(j,Color(i,0,0))
        strip.show()
        time.sleep(0.01)
    for i in range(green*int(unit)):
        for j in range(LED_COUNT):
            strip.setPixelColor(j,Color(red*int(unit),i,0))
        strip.show()
        time.sleep(0.01)
    for i in range(blue*int(unit)):
        for j in range(LED_COUNT):
            strip.setPixelColor(j,Color(red*int(unit),green*int(unit),i))
        strip.show()
        time.sleep(0.01)
    for i in range(red*int(unit),-1,-1):
        for j in range(LED_COUNT):
            strip.setPixelColor(j,Color(i,green*int(unit),blue*int(unit)))
        strip.show()
        time.sleep(0.01)
    for i in range(green*int(unit),-1,-1):
        for j in range(LED_COUNT):
            strip.setPixelColor(j,Color(0,i,blue*int(unit)))
        strip.show()
        time.sleep(0.01)
    for i in range(blue*int(unit),-1,-1):
        for j in range(LED_COUNT):
            strip.setPixelColor(j,Color(0,0,i))
        strip.show()
        time.sleep(0.01)
def color(brightness):
    red = random.randint(0,20)
    green = random.randint(0,20)
    blue = random.randint(0,20)
    unit = brightness / (red+green+blue)
    return Color(red*int(unit),green*int(unit),blue*int(unit))

def on_off():
    traveler = 0
    use_color = color(200)
    for j in range(LED_COUNT):
        for i in range(LED_COUNT):
            if i == traveler:
                strip.setPixelColor(i,use_color)
        strip.show()
        time.sleep(0.05)
        traveler = traveler + 1
    traveler = 0
    for j in range(LED_COUNT):
        for i in range(LED_COUNT):
            if i == traveler:
                strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(0.05)
        traveler = traveler + 1
        
def travelers():
    for j in range(100):
        mod = j%3
        for i in range(LED_COUNT):
            if i % 3 == mod:
                strip.setPixelColor(i,color(200))
            else:
                strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(0.1)
        
def explosion():
    traveler = 0;
    clear()
    for j in range(int(LED_COUNT/2)+1):
        for i in range(int(LED_COUNT/2)+1):
            strip.setPixelColor(i,Color(0,0,0))
            strip.setPixelColor(LED_COUNT - i,Color(0,0,0))
            if i == traveler:
                strip.setPixelColor(i,Color(90,70,10))
                strip.setPixelColor(LED_COUNT - i,Color(90,70,10))
            else:
                strip.setPixelColor(i,Color(0,0,0))
                strip.setPixelColor(LED_COUNT - i,Color(0,0,0))
        traveler = traveler + 1
        strip.show()
        time.sleep(0.05)
    for i in range(200,-1,-1):
            for j in range(LED_COUNT):
                strip.setPixelColor(j,Color(i+50,i,0))
            strip.show()
            time.sleep(0.02)
    for i in range(50,-1,-1):
            for j in range(LED_COUNT):
                strip.setPixelColor(j,Color(i,0,0))
            strip.show()
            time.sleep(0.02)
            
def spiral():
    use_color = color(200)
    for j in range(30,0,-1):
        mod = j%3
        for i in range(LED_COUNT):
            if i % 3 == mod:
                strip.setPixelColor(i,use_color)
            else:
                strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(pow(j,2)/1500)
    for j in range(20):
        mod = j%3
        for i in range(LED_COUNT):
            if i % 3 == mod:
                strip.setPixelColor(i,use_color)
            else:
                strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(pow(j,2)/1000)    
    for j in range(100,0,-1):
        mod = j%3
        for i in range(LED_COUNT):
            if i % 3 == mod:
                strip.setPixelColor(i,use_color)
            else:
                strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(pow((j/6),2)/1500)
    clear()
    
def bubble_sort():
    color1 = Color(200,0,0)
    color2 = Color(0,0,200)
    table = []
    for i in range(LED_COUNT):
        table.append((i,200-(i*2),i*2))
    unsorted = []
    while True:
        rand = random.randint(0,99)
        if rand in unsorted:
            continue
        else:
            unsorted.append(rand)
        if len(unsorted) == 100:
            break
    for i in range(LED_COUNT):
        strip.setPixelColor(i,Color(table[unsorted[i]][1],table[unsorted[i]][2],0))
    strip.show()
    time.sleep(1)
    for i in range(LED_COUNT):
        for j in range(LED_COUNT-1):
            if unsorted[j] > unsorted[j+1]:
                pomocnik = unsorted[j+1]
                unsorted[j+1]=unsorted[j]
                unsorted[j]=pomocnik
        for j in range(LED_COUNT):
            strip.setPixelColor(j,Color(table[unsorted[j]][1],table[unsorted[j]][2],0))
        strip.show()
        time.sleep(0.1)
    for j in range(LED_COUNT):
        strip.setPixelColor(j,Color(0,0,0))
    strip.show()
    time.sleep(0.5)
    for j in range(LED_COUNT):
        strip.setPixelColor(j,Color(table[j][1],table[j][2],0))
    strip.show()
    time.sleep(1)
def clear():
    for i in range(LED_COUNT):
        strip.setPixelColor(i,Color(0,0,0))
    strip.show()
