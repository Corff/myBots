import pybullet as p
import pybullet_data
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = p.loadURDF("plane.urdf")
bodyID = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")

for i in range(0,1000):
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect()