from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import sys

from Models import Tray, Ball
from Camera import Camera
from utils import Color
from Interface import Scoreboard
from Gamesound import Sound

class Viewer:
    def __init__(self):
        
        #################################################
        self.interface = Scoreboard(6,3,0.3)
        self.sound = Sound()
        #################################################
        
        self.tray = Tray(8)
        self.camera = Camera()
        self.balls = [
            Ball(1, Color.GREEN.value, np.array([0, 10, 0], dtype=np.float64)),
            Ball(0.75, Color.YELLOW.value, np.array([-3, 6, 0], dtype=np.float64)),
            Ball(0.4, Color.RED.value, np.array([2, 1, 2], dtype=np.float64))
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
        self.tray.create()

    ## Draws one frame, the tray then the balls, from the current camera position.
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(self.camera.getX(), self.camera.getY(), self.camera.getZ(),
                    0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0)
        self.tray.draw()
        
        #################################################
        self.interface.draw()
        for ball in self.balls:
            if ball.colisionchecker() == 1:
                self.sound.bounceball()
            if ball.colisionchecker() == 2:
                self.sound.bounceball_s()
        #################################################
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


    ########################
    # 임시로 만듬 pygame handler
    ########################
    def keyboard(self, key, x, y):
        if key == b'q':
            self.sound.quit()
            



    ## Moves the camera according to the key pressed, then ask to refresh the display.
    def special(self, key, x, y):
        if key == GLUT_KEY_LEFT:
            self.camera.moveLeft()
        elif key == GLUT_KEY_RIGHT:
            self.camera.moveRight()
        elif key == GLUT_KEY_UP:
            self.camera.moveUp()
        elif key == GLUT_KEY_DOWN:
            self.camera.moveDown()
        glutPostRedisplay()


    def run(self):
        glutInit()                                                  # ? -> maybe initialize gl utilities ?
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )  # ?
        glutInitWindowSize(1200, 840)                                # Set the initial window size
        glutInitWindowPosition(0, 0)                                # Set the initial position of window
        glutCreateWindow(b"Computer Graphics Final Project")        # Create window with the title

        glutDisplayFunc(self.display)           # Bind the display function
        glutReshapeFunc(self.reshape)           # Bind the Reshape function
        glutSpecialFunc(self.special)           # Bind the special key function
        glutTimerFunc(100, self.timer, 0)       # Start the timer
        
        ###############################
        glutKeyboardFunc(self.keyboard)
        # self.sound.play()
        ###############################

        self.init()
        glutMainLoop()                          # Make the program not terminate
