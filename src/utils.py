from enum import Enum

WINDOW_SIZE = 800

class Color(Enum):
    WHITE   = [1, 1, 1]
    RED     = [255/256, 158/256, 158/256]  # rgb(255, 158, 158)
    GREEN   = [192/256, 238/256, 228/256]   # rgb(192, 238, 228)
    YELLOW  = [248/256, 249/256, 136/256]   # rgb(248, 249, 136)
    MAGENTA = [1, 0, 1]
    GREY    = [0.4, 0.4, 0.4]