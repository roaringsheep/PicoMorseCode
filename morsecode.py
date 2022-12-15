from machine import Pin
import time

led = Pin(25, Pin.OUT)

def short():
    led.value(1)
    time.sleep(1/3)
    led.value(0)
    time.sleep(1/3)

def long():
    led.value(1)
    time.sleep(2/3)
    led.value(0)
    time.sleep(1/3)
    
def charBreak():
    time.sleep(1/2)

def wordBreak():
    time.sleep(1)
def A():
    short()
    long()
    charBreak()
    
def B():
    long()
    for i in range(3):
        short()
    charBreak()

def C():
    long()
    short()
    long()
    short()
    charBreak()

def D():
    long()
    short()
    short()
    charBreak()

def E():
    short()
    charBreak()
    
def F():
    short()
    short()
    long()
    short()

def H():
    for i in range(4):
        short()
    charBreak()


def L():
    short()
    long()
    short()
    short()

def O():
    for i in range(3):
        long()
    
def W():
    short()
    long()
    long()
    
def R():
    short()
    long()
    short()

    
charDict = {
    'a': A,
    'b': B,
    'c': C,
    'd': D,
    'e': E,
    'f': F,
    'g': G,
    'h': H,
    'i': I,
    'j': J,
    'k': K,
    'l': L,
    'm': M,
    'n': N,
    'o': O,
    'p': P,
    'q': Q,
    'r': R,
    's': S,
    't': T,
    'u': U,
    'v': V,
    'w': W,
    'x': X,
    'y': Y,
    'z': Z
}

def StrToMorse(str):
    str = str.lower()
    for c in str:
        if c in string.ascii_letters:
            charDict[c]()
        elif c in string.whitespace(c):
            wordBreak()

