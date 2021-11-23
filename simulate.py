import pybullet as p
import pybullet_data
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = p.loadURDF("plane.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("box.sdf")

for i in range(0,1000):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()