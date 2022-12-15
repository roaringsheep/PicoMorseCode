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
    time.sleep(2)
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
    charBreak()
    
def G():
    long()
    long()
    short()
    charBreak()

def H():
    for i in range(4):
        short()
    charBreak()

def I():
    short()
    short()

def J():
    short()
    for i in range(3):
        long()
    charBreak()

def K():
    long()
    short()
    long()
    charBreak()

def L():
    short()
    long()
    short()
    short()
    charBreak()

def M():
    long()
    long()
    charBreak()

def N():
    long()
    short()
    charBreak()

def O():
    for i in range(3):
        long()
    charBreak()

def P():
    short()
    long()
    long()
    short()
    charBreak()

def Q():
    long()
    long()
    short()
    long()
    charBreak()

def R():
    short()
    long()
    short()
    charBreak()
    
def S():
    for i in range(3):
        short()
    charBreak()

def T():
    long()
    charBreak()

def U():
    short()
    short()
    long()
    charBreak()

def V():
    for i in range(3):
        short()
    charBreak()

def W():
    short()
    long()
    long()
    charBreak()
    
def X():
    long()
    short()
    short()
    long()
    charBreak()

def Y():
    long()
    short()
    long()
    long()
    charBreak()

def Z():
    long()
    long()
    short()
    short()
    charBreak()

    
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
        if c.isalpha():
            charDict[c]()
        elif c.isspace():
            wordBreak()

StrToMorse("Hello World")