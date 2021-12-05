import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

pi = 3.14159265359
steps = 1000
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
backLegSensorValues = np.zeros(steps)
frontLegSensorValues = np.zeros(steps)
x = np.linspace(-np.pi, np.pi, 201)

for i in range(0,steps):
    p.stepSimulation()

    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = "Torso BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-pi/2,pi/2),
        maxForce = 25
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = "Torso FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition= random.uniform(-pi/2,pi/2),
        maxForce = 25
    )

    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)

p.disconnect()

np.save("data/backLegSensorValues.npy",backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)


#print(backlogSensorValues)