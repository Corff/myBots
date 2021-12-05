import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import sys

print(sys.executable)

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = p.loadURDF("plane.urdf")
bodyID = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backlogSensorValues = numpy.zeros(10000)

for i in range(0,1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    print(backLegTouch)
    time.sleep(1/60)

p.disconnect()