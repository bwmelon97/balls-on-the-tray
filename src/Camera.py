import math

class Camera():
    def __init__(self,
                 dist: float = 20,
                 theta: float = math.pi * (1 / 2),
                 y: float = 10,
                 dTheta: float = 0.04,
                 dy: float = 0.1):
        self.dist = dist            # determines the x and z distance
        self.theta = theta          # determines the x and z angle
        self.y = y                  # the current y position
        self.dTheta = dTheta        # increment in theta for swinging the camera around
        self.dy = dy                # increment in y for moving the camera up/down

    def getX(self):
        return self.dist * math.cos(self.theta)

    def getY(self):
        return self.y

    def getZ(self):
        return self.dist * math.sin(self.theta)


    ## Methods to set the camera position
    ## This methods used to check the initial setting for developing,
    ## but they are not used in the user's playtime.
    def moveRight(self):
        self.theta = self.theta + self.dTheta

    def moveLeft(self):
        self.theta = self.theta - self.dTheta

    def moveUp(self):
        self.y = self.y + self.dy

    def moveDown(self):
        if (self.y > self.dy):
            self.y = self.y - self.dy