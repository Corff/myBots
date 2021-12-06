import pyrosim.pyrosim as ps
import constants as c
import numpy as np
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.steps)

    def Set_Value(self, robot, desiredAngle):
        ps.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = desiredAngle, maxForce = c.maxForce)
