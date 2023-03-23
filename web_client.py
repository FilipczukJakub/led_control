import asyncio
import websockets
import time
import threading
import board
#import neopixel
import random
import new_test
#pixels = neopixel.NeoPixel(board.D18,300)
stop = bool(0)
def standby():
    while True:
        new_test.idle()
        if stop:
            print("Zakończono idle")
            break
async def hello():
    while True:
        try:
            async with websockets.connect("ws://91.210.51.24:5000") as websocket:
                await websocket.send("###raspberry###")
                while True: 
                    message = await websocket.recv()
                    print(message)
                    global stop
                    global t1
                    if message == "1":
                        stop = bool(1)
                        print("Tryb 1")
                        while t1.is_alive():
                            continue
                        new_test.clear()
                        new_test.on_off()
                        stop = bool(0)
                        t1 = threading.Thread(target=standby, args=())
                        t1.start()
                    elif message == "2":
                        stop = bool(1)
                        print("Tryb 2")
                        while t1.is_alive():
                            continue
                        new_test.clear()
                        new_test.travelers()
                        stop = bool(0)
                        t1 = threading.Thread(target=standby, args=())
                        t1.start()
                    elif message == "3":
                        stop = bool(1)
                        print("Tryb 3")
                        while t1.is_alive():
                            continue
                        new_test.clear()
                        new_test.explosion()
                        stop = bool(0)
                        t1 = threading.Thread(target=standby, args=())
                        t1.start()
                    elif message == "4":
                        stop = bool(1)
                        print("Tryb 4")
                        while t1.is_alive():
                            continue
                        new_test.clear()
                        new_test.spiral()
                        stop = bool(0)
                        t1 = threading.Thread(target=standby, args=())
                        t1.start()
                    elif message == "5":
                        stop = bool(1)
                        print("Tryb 5")
                        while t1.is_alive():
                            continue
                        new_test.clear()
                        new_test.bubble_sort()
                        stop = bool(0)
                        t1 = threading.Thread(target=standby, args=())
                        t1.start()
        except:
            print("Utracono połączenie z serverem")
            stop = bool(1)
            while t1.is_alive():
                continue
            stop = bool(0)
            t1 = threading.Thread(target=standby, args=())
            t1.start()
            continue
if __name__ == "__main__":
    global t1
    new_test.clear()
    t1 = threading.Thread(target=standby, args=())
    t1.start()
    asyncio.run(hello())

