import time
import socket
import json
import threading
import importlib
import os
import subprocess
import sys
from tkinter import *
import math
from random import randint
from queue import Queue
from pynput.keyboard import Key, Controller
from directkeys import PressKey, ReleaseKey, W, A, S, D, Z, R, LEFT, RIGHT, UP, DOWN, SPACE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6789))
# s.setblocking(False)

keyboard = Controller()

def getInput():
    while 1:
        rec = s.recv(1024)
        decodeMsg = list(filter(None, rec.split(b'\r\n\r\n')))[0]
        dictionary = json.loads(decodeMsg)
        recKey = dictionary.get("key")
        
        if recKey == "right":
                PressKey(RIGHT)
                ReleaseKey(RIGHT)
        elif recKey == "left":
                PressKey(LEFT)
                ReleaseKey(LEFT)
        elif recKey == "up":
                PressKey(UP)
                ReleaseKey(UP)
        elif recKey == "down":
                PressKey(DOWN)
                ReleaseKey(DOWN)
        elif recKey == "z":
                PressKey(Z)
                ReleaseKey(Z)
        elif recKey == "r":
                PressKey(R)
                ReleaseKey(R)
        elif recKey == "space":
                PressKey(SPACE)
                ReleaseKey(SPACE)

        # elif recKey == "w":
        #         PressKey(W)
        #         ReleaseKey(W)


getInput()