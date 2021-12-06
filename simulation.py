from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data as pb
import pyrosim
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pb.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
    def Run(self):
        for i in range(0,c.steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(c.sleepTime)
        self.__del__()
        
    
    def __del__(self):
        self.physicsClient.disconnect()