import ctypes
import time

#dicionário definições
teclas = dict()
teclas["up"] = (0x48,True)
teclas["down"] = (0x50,True)
teclas["left"] = (0x4B,True)
teclas["right"] = (0x4D,True)
teclas["insert"] = (0x52,True)
teclas["delete"] = (0x53,True)
teclas["esc"] = (0x01,False)
teclas["1"] = (0x02,False)
teclas["2"] = (0x03,False)
teclas["3"] = (0x04,False)
teclas["4"] = (0x05,False)
teclas["5"] = (0x06,False)
teclas["6"] = (0x07,False)
teclas["7"] = (0x08,False)
teclas["8"] = (0x09,False)
teclas["9"] = (0x0A,False)
teclas["0"] = (0x0B,False)
teclas["-"] = (0x0C,False)
teclas["+"] = (0x0D,False)
teclas["backspace"] = (0x0E,False)
teclas["tab"] = (0x0F,False)
teclas["q"] = (0x10,False)
teclas["w"] = (0x11,False)
teclas["e"] = (0x12,False)
teclas["r"] = (0x13,False)
teclas["t"] = (0x14,False)
teclas["y"] = (0x15,False)
teclas["u"] = (0x16,False)
teclas["i"] = (0x17,False)
teclas["o"] = (0x18,False)
teclas["´"] = (0x1A,False)
teclas["["] = (0x1B,False)
teclas["enter"] = (0x1C,False)
teclas["ctrl"] = (0x1D,False)
teclas["a"] = (0x1E,False)
teclas["s"] = (0x1F,False)
teclas["d"] = (0x20,False)
teclas["f"] = (0x21,False)
teclas["g"] = (0x22,False)
teclas["h"] = (0x23,False)
teclas["j"] = (0x24,False)
teclas["k"] = (0x25,False)
teclas["l"] = (0x26,False)
teclas["ç"] = (0x27,False)
teclas["~"] = (0x28,False)
teclas["'"] = (0x29,False)
teclas["shift"] = (0x2A,False)
teclas["]"] = (0x2B,False)
teclas["z"] = (0x2C,False)
teclas["x"] = (0x2D,False)
teclas["c"] = (0x2E,False)
teclas["v"] = (0x2F,False)
teclas["b"] = (0x30,False)
teclas["n"] = (0x31,False)
teclas["m"] = (0x32,False)
teclas[","] = (0x33,False)
teclas["."] = (0x34,False)
teclas[";"] = (0x35,False)
teclas["alt"] = (0x38,False)
teclas["space"] = (0x39,False)
teclas["capslock"] = (0x3A,False)

SendInput = ctypes.windll.user32.SendInput

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
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions


def pressKey(hexKeyCode,extendido = False):
    extensao = 0x0008
    if(extendido == True):
        extensao = 0x0001
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0,hexKeyCode, (extensao | 0x0008), 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def releaseKey(hexKeyCode,extendido = False):
    extensao = 0x0008
    if(extendido == True):
        extensao = 0x0001
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0,hexKeyCode, (extensao | 0x0008)| 0x0002, 0, 
ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

