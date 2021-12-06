import pybullet as p
import pyrosim.pyrosim as ps
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        ps.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in ps.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self,t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in ps.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    def Act(self, t):
        for i in self.motors:
            self.motors[i].Set_Value(self.robot, t)