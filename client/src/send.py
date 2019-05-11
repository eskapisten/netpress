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


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6789))
s.setblocking(False)

WIDTH = 500
HEIGHT = 500

root = Tk()

mainFrame = Frame(root, width = WIDTH, height = HEIGHT)
mainFrame.pack()
mainFrame.focus_force()

def keyPressed(key):
    sendKey = {"key": key}
    jsonMessage = json.dumps(sendKey).encode()
    data = jsonMessage + b"\r\n\r\n"
    s.send(data)

mainFrame.bind("<KeyPress-Right>", lambda event: keyPressed("right"))
mainFrame.bind("<KeyPress-Left>", lambda event: keyPressed("left"))
mainFrame.bind("<KeyPress-Up>", lambda event: keyPressed("up"))
mainFrame.bind("<KeyPress-Down>", lambda event: keyPressed("down"))
mainFrame.bind("<KeyPress-z>", lambda event: keyPressed("z"))
mainFrame.bind("<KeyPress-r>", lambda event: keyPressed("r"))
# mainFrame.bind("<KeyPress-w>", lambda event: keyPressed("w"))
# mainFrame.bind("<KeyPress-a>", lambda event: keyPressed("a"))
# mainFrame.bind("<KeyPress-s>", lambda event: keyPressed("s"))
# mainFrame.bind("<KeyPress-d>", lambda event: keyPressed("d"))
mainFrame.bind("<space>", lambda event: keyPressed("space"))

root.mainloop()