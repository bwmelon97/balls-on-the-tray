from __future__ import annotations 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import math

from utils import Color, RotateSignal
from Interface import Player


## A ball. A ball has a radius, a color, a position and its velocity. 
class Ball():
    def __init__(self,
                 radius: float,
                 color: list[float],
                 position: np.ndarray,
                 tray: Tray):
        self.radius = radius
        self.color = color
        self.position = position
        self.tray = tray

        ##############################################################################
        self.colisioncheck = 0
        ##############################################################################
        
        
        ## properties for movement
        self.v = np.array([0, 0, 0], dtype=np.float64)   # velocity
        

    ## update the position of the ball for each frame
    ## updated position = position + velocity
    def update(self):
        n = self.tray.getNormalVec()[:3]                        # normal vector of the plain

        ## params for physics
        g_p = 1000      # Gravity
        f_p = 0.98      # Friction
        e_p = 0.3       # elasticity

        g = np.array([0, -9.8, 0], dtype=np.float64) / g_p      # gravity acceleration (dv)
        self.v += g                                             # add g to the v

        ## v can devide into vn and vt (v = vn + vt)
        vn = n * np.dot(self.v, n)                              # n direction vecotr of v
        vt = self.v - vn                                        # vt = v - vn
        vt = vt * f_p                                           # frictional force

        ## Collision detection
        ## if the shpere is in the tray and under the plane, reflect the vn
        o_dist = np.linalg.norm(self.position)                      # distance between the centor of sphere and the origin
        p_dist = np.dot(n, self.position) / (np.linalg.norm(n))     # distance between the center of sphere and the plane

        ball_is_in_tray = o_dist <= math.sqrt(self.radius ** 2 +    # Check if the ball is in the tray
                                           self.tray.radius ** 2)   #     o_dist < sqrt(s_r^2 + t_r^2)
        under_tray = p_dist < self.radius                           # Check if the ball is under the tray

        if ball_is_in_tray and under_tray:
            vn = -vn * e_p
            ## 공을 평면 아래에서 평면의 접점 위치로 올려놓지 않으면,
            ## 올라오는 vn보다 새로 가해지는 중력이 더 크기 때문에 공이 가라앉음
            self.position = self.position + (n * (self.radius - p_dist))
        
        ##############################################################################
        if dist == self.radius and self.v[1] >= -0.001:
            if abs(self.v[1]) >= 0.008:
                if self.radius > 0.7:
                    self.colisioncheck = 1
                if self.radius <= 0.7:
                    self.colisioncheck = 2
        else:
            self.colisioncheck = 0
        ##############################################################################
        
        self.v = vn + vt
        self.position = self.position + self.v
        self.render()
        
    ## Render the ball
    def render(self):
        x, y, z = self.position
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.color)
        glTranslated(x, y, z)
        glutSolidSphere(self.radius, 30, 30)
        glPopMatrix()
        
    def colisionchecker(self):
        if self.colisioncheck == 1:
            print("colision v : ", self.v[1])
            return 1



## A Tray. One corner of the board is (0, 0) and the board stretches out
## along positive x and positive z.  It rests on the xz plane.  I put a
## spotlight at (4, 3, 7).
class Tray():
    def __init__(self, radius: float = 10):
        self.radius = radius
        self.n = np.array([0, 1, 0, 0])
        self.R = np.eye(4)

    def getNormalVec(self) -> np.ndarray:
        return self.R @ self.n

    def render(self):
        # Spot light
        lightPosition = [5, 15, 5, 1]
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)

        glPushMatrix()
        glMultMatrixf(self.R.T)

        glBegin(GL_TRIANGLE_FAN)
        glNormal3d(0, 1, 0)

        sharp = 100                 # Sharpness(선명도) of Ellipse
        cycle_degree = 2 * math.pi  # 1 cycle degree = 2 pi
        
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, Color.GREY.value)
        glVertex3f(0, 0, 0)         # centor coordinate
        for i in range(sharp + 1):
            unit_theta = cycle_degree / sharp
            glVertex3f (
                self.radius * math.cos( i * unit_theta ),  # x = r * cos(theta)
                0,
                self.radius * math.sin( i * unit_theta ),  # z = r * sin(theta)
            )
        glEnd()
        glPopMatrix()

    def rotate(self, x_sig: RotateSignal, z_sig: RotateSignal):
        theta = -(1 / 50)

        ## 위 아래 키 입력인 경우, yz plane을 따라 회전
        if x_sig.value == RotateSignal.ZERO.value:
            if z_sig.value == RotateSignal.NEG.value:
                theta = -theta
            dR = np.array([[1, 0,               0,                0],
                           [0, math.cos(theta), -math.sin(theta), 0],
                           [0, math.sin(theta), math.cos(theta),  0],
                           [0, 0,               0,                1]])

        ## 좌우 키 입력인 경우, xy plane을 따라 회적
        else:
            if x_sig.value == RotateSignal.NEG.value:
                theta = -theta
            dR = np.array([[math.cos(theta), -math.sin(theta), 0, 0],
                           [math.sin(theta), math.cos(theta),  0, 0],
                           [0,               0,                1, 0],
                           [0,               0,                0, 1]])

        self.R = dR @ self.R

class Basket():
    def __init__(self,
                 player: Player,
                 position: np.ndarray,
                 color: Color,
                 radius: float = 3.0):
        self.player = player
        self.position = position
        self.color = color
        self.radius = radius

    def change_position(self, position: np.ndarray):
        self.position = position

    def render(self):
        x, y, z = self.position

        ## Basket의 옆면 (Torus * 100으로 구현)
        for i in range(100):
            glPushMatrix()
            glTranslated(x, y - (i * 0.05), z)
            glRotated(-90, 1.0, 0.0, 0.0)
            glNormal3d(0, 1, 0)
            glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.color)
            glutSolidTorus(0.1, self.radius, 10, 50)
            glPopMatrix()

        ## Bottom of the basket
        glPushMatrix()
        glTranslated(x, y - 5, z)   # Basket 바닥으로 이동
        glBegin(GL_TRIANGLE_FAN)
        glNormal3d(0, 1, 0)
        sharp = 100                 # Sharpness(선명도) of Ellipse
        cycle_degree = 2 * math.pi  # 1 cycle degree = 2 pi
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.color)
        glVertex3f(0, 0, 0)         # centor coordinate
        for i in range(sharp + 1):
            unit_theta = cycle_degree / sharp
            glVertex3f (
                self.radius * math.cos( i * unit_theta ),  # x = r * cos(theta)
                0,
                self.radius * math.sin( i * unit_theta ),  # z = r * sin(theta)
            )
        glEnd()
        glPopMatrix()
