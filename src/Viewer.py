from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import sys

from Models import Tray, Ball, Basket
from Camera import Camera
from Interface import Interface, Player
from Gamesound import Sound
from utils import *

class Viewer:
    def __init__(self):
        
        self.player1 = Player(PlayerId.ONE)
        self.player2 = Player(PlayerId.TWO)
        self.baskets = [
            Basket(self.player1, np.array([-10, -12, 0], np.float64), Color.LIGHT_BLUE.value),
            Basket(self.player2, np.array([10, -12, 0], np.float64), Color.RED.value),
        ]

        self.interface = Interface(self.player1, self.player2)

        self.tray = Tray(8)
        self.camera = Camera()
        self.balls = [
            Ball(1.0, Color.GREEN.value, np.array([0, 8, 0], dtype=np.float64), self.tray, self.baskets, 1),
            # Ball(0.7, Color.YELLOW.value, np.array([-3, 7, 0], dtype=np.float64), self.tray, self.baskets, 2),
            Ball(0.4, Color.RED.value, np.array([2, 5, 2], dtype=np.float64), self.tray, self.baskets, 3)
        ]

    ## Application-specific initialization: Set up global lighting parameters
    ## and create display lists.
    def init(self):
        glEnable(GL_DEPTH_TEST)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1])
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1])
        glMaterialf(GL_FRONT, GL_SHININESS, 30)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    ## Draws one frame, the tray then the balls, from the current camera position.
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(self.camera.getX(), self.camera.getY(), self.camera.getZ(),
                    0.0, -5.0, 0.0,     ## Tray를 스크린 상 위쪽에 위치하도록 함
                    0.0, 1.0, 0.0)

        self.interface.draw_scoreboard()
        self.tray.render()
        for basket in self.baskets:
            basket.render()
        if self.interface.is_play == True:
            for ball in self.balls:
                ball.update()

        glFlush()
        glutSwapBuffers()

    ## On reshape, constructs a camera that perfectly fits the window.
    def reshape(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, w / h, 1.0, 150.0)
        glMatrixMode(GL_MODELVIEW)

    ## Requests to draw the next frame.
    def timer(self, v):
        glutPostRedisplay()
        glutTimerFunc(20, self.timer, 0)   # 50 updates per 1 sec

    ## Keyboard handler. wasd for moving the tray, p for quit the sound
    def keyboard(self, key, x, y):
        if key == b'a':
            self.tray.rotate(RotateSignal.NEG, RotateSignal.ZERO)
        elif key == b'd':
            self.tray.rotate(RotateSignal.POS, RotateSignal.ZERO)
        elif key == b'w':
            self.tray.rotate(RotateSignal.ZERO, RotateSignal.POS)
        elif key == b's':
            self.tray.rotate(RotateSignal.ZERO, RotateSignal.NEG)
        if self.interface.is_play == False and self.interface.remain_time > 0:
            self.interface.start()
        glutPostRedisplay()

    ## special key handler. Arrows for moving the tray
    def special(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.tray.rotate(RotateSignal.NEG, RotateSignal.ZERO)
        elif key == GLUT_KEY_RIGHT:
            self.tray.rotate(RotateSignal.POS, RotateSignal.ZERO)
        elif key == GLUT_KEY_UP:
            self.tray.rotate(RotateSignal.ZERO, RotateSignal.POS)
        elif key == GLUT_KEY_DOWN:
            self.tray.rotate(RotateSignal.ZERO, RotateSignal.NEG)
        if self.interface.is_play == False and self.interface.remain_time > 0:
            self.interface.start()
        glutPostRedisplay()


    def run(self):
        glutInit()                                                  # ? -> maybe initialize gl utilities ?
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )  # ?
        glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)             # Set the initial window size
        glutInitWindowPosition(0, 0)                                # Set the initial position of window
        glutCreateWindow(b"Computer Graphics Final Project")        # Create window with the title

        glutDisplayFunc(self.display)           # Bind the display function
        glutReshapeFunc(self.reshape)           # Bind the Reshape function
        glutKeyboardFunc(self.keyboard)         # Bind the keyboard function
        glutSpecialFunc(self.special)           # Bind the special key function
        glutTimerFunc(100, self.timer, 0)       # Start the timer
        
        ###############################
        glutKeyboardFunc(self.keyboard)
        # self.sound.play()
        ###############################

        self.init()
        glutMainLoop()                          # Make the program not terminate
