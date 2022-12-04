from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from enum import Enum
import numpy as np

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 840

class Color(Enum):
    WHITE       = [1, 1, 1]
    RED         = [255/256, 158/256, 158/256]   # rgb(255, 158, 158)
    LIGHT_BLUE  = [185/256, 224/256, 255/256]   # rgb(185, 224, 255)
    GREEN       = [192/256, 238/256, 228/256]   # rgb(192, 238, 228)
    YELLOW      = [248/256, 249/256, 136/256]   # rgb(248, 249, 136)
    GREY        = [0.4, 0.4, 0.4]
    BLACK       = [0, 0, 0]

class RotateSignal(Enum):
    NEG     = -1        # Negative signal
    ZERO    = 0         # No Input signal
    POS     = 1         # Positive signal

class PlayerId(Enum):
    ONE = 1
    TWO = 2

def drawText(position: np.ndarray, text: str, color: Color = Color.WHITE.value):
    '''
    postion: Text Position
    text: content of the text
    color: color of the text

    Render a text object
    '''
    x, y, z = position
    r, g, b = color

    glPushMatrix()
    glDisable(GL_LIGHTING)
    glColor3f(r, g, b)
    glRasterPos3f(x, y, z)
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
    glEnable(GL_LIGHTING)
    glPopMatrix()