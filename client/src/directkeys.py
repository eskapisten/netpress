# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
import time
import pynput

SendInput = ctypes.windll.user32.SendInput


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Z = 0x2C
R = 0x13
LEFT = 0xCB
RIGHT = 0xCD
UP = 0xC8
DOWN = 0xD0
SPACE = 0x39

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.culong(0)
    ii = pynput._util.win32.INPUTunion()
    ii.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.culong(1), ii)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.culong(0)
    ii = pynput._util.win32.INPUTunion()
    ii.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.culong(1), ii)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# def PressKey(hexKeyCode):
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(1), ii_)
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# def ReleaseKey(hexKeyCode):
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002,
#                         0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(1), ii_)
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# if __name__ == '__main__':
#     PressKey(0x11)
#     time.sleep(1)
#     ReleaseKey(0x11)
#     time.sleep(1)