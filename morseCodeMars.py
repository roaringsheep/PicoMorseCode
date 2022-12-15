from machine import Pin
import time


led = Pin(25, Pin.OUT)

def long():
    time.sleep(0.5)
    led.value(1)
    time.sleep(1.5)
    led.value(0)

def short():
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    
    
def letterSpace():
    time.sleep(1)

def wordSpace():
    time.sleep(3)
    
def H():
    for x in range(4):
        short()
    letterSpace()

def E():
    short()
    letterSpace()
    
def L():
    short()
    long()
    short()
    short()
    letterSpace()

def O():
    for x in range(3):
        long()
    letterSpace()
    
def W():
    short()
    long()
    long()
    letterSpace()
    
def R():
    short()
    long()
    short()
    letterSpace()
    
def D():
    long()
    short()
    short()
    letterSpace()

def A():
    short()
    long()
    letterSpace()
    
def B():
    long()
    for x in range(3):
        short()
    letterSpace()
    
def C():
    for x in range(2):
        long()
        short()
    letterSpace()

def F():
    short()
    short()
    long()
    short()
    letterSpace()

def G():
    long()
    long()
    short()
    letterSpace()
    
def I():
    short()
    short()
    letterSpace()

def J():
    short()
    for x in range(3):
        long()
    letterSpace()

def K():
    long()
    short()
    long()
    letterSpace()

def M():
    long()
    long()
    letterSpace()

def N():
    long()
    short()
    letterSpace()
    
def P():
    short()
    long()
    long()
    short()
    letterSpace()
    
def Q():
    long()
    long()
    short()
    long()
    letterSpace()

def S():
    short()
    short()
    short()
    letterSpace()

def T():
    long()
    letterSpace()
    
def U():
    short()
    short()
    long()
    letterSpace()
    
def V():
    short()
    short()
    short()
    long()
    letterSpace()

def X():
    long()
    short()
    short()
    long()
    letterSpace()
    
def Y():
    long()
    short()
    long()
    long()
    letterSpace()
    
def Z():
    long()
    long()
    short()
    short()
    letterSpace()

symbols = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
    "H": H,
    "I": I,
    "J": J,
    "K": K,
    "L": L,
    "M": M,
    "N": N,
    "O": O,
    "P": P,
    "Q": Q,
    "R": R,
    "S": S,
    "T": T,
    "U": U,
    "V": V,
    "W": W,
    "X": X,
    "Y": Y,
    "Z": Z,
    " ": wordSpace
    }

def stringToMorse(message):
    message = message.upper()
    for c in message:
        symbols[c]()

stringToMorse("Hello World")

    
