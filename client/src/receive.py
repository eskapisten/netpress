import time
import socket
import json
import threading
import importlib
import os
import pygame
import subprocess
import sys
from tkinter import *
import math
from random import randint
from queue import Queue
from pynput.keyboard import Key, Controller


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
        
        time.sleep(3)
        if recKey == "right":
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        elif recKey == "left":
                keyboard.press(Key.left)
                keyboard.release(Key.left)
        elif recKey == "up":
                keyboard.press(Key.up)
                keyboard.release(Key.up)
        elif recKey == "down":
                keyboard.press(Key.down)
                keyboard.release(Key.down)
        elif recKey == "z":
                keyboard.press('z')
                keyboard.release('z')
        elif recKey == "r":
                keyboard.press('r')
                keyboard.release('r')


getInput()