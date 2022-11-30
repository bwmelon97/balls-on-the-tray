from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from utils import *

class Viewer:
    def __init__(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)      # ? -> maybe initialize?
        glClearColor(0, 0, 0, 1)                                # Set the background color (maybe)

        glutSwapBuffers()   # ? -> It must be executed, to apply the change (maybe)

    def run(self):
        glutInit()                                                  # ? -> maybe initialize gl utilities ?
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )  # ?
        glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)                # Set the initial window size
        glutInitWindowPosition(0, 0)                                # Set the initial position of window
        glutCreateWindow(b"Computer Graphics Final Project")        # Create window with the title

        glutDisplayFunc(self.display)           # Bind the display function

        glutMainLoop()                          # Make the program not terminate