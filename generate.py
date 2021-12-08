import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="box", pos=[5,0,0.5], size = [1,1,1])
    pyrosim.End()

def Create_Robot():#forwardback, leftright, updown
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size = [1,.5,.5])

    pyrosim.Send_Joint(name="Torso_FLT", parent="Torso", child="FLT", type="revolute", position="-.425 0.1775 0.875")
    pyrosim.Send_Cube(name="FLT", pos=[-0.1, 0.1, 0], size=[0.15, 0.15, 0.75])
    pyrosim.Send_Joint(name="FLT_FLL", parent="FLT", child="FLL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="FLL", pos=[-0.1, 0.1, 0], size=[0.1, 0.1, 0.5])

    pyrosim.Send_Joint(name="Torso_FRT", parent="Torso", child="FRT", type="revolute", position="-.425 -0.1775 0.875")
    pyrosim.Send_Cube(name="FRT", pos=[-0.1, -0.1, 0], size=[0.15, 0.15, 0.75])
    pyrosim.Send_Joint(name="FRT_FRL", parent="FRT", child="FRL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="FRL", pos=[-0.1, -0.1, 0], size=[0.1, 0.1, 0.5])

    pyrosim.Send_Joint(name="Torso_BLT", parent="Torso", child="BLT", type="revolute", position=".425 0.1775 1")
    pyrosim.Send_Cube(name="BLT", pos=[-0.1, 0.1, 0], size=[0.15, 0.15, 0.5])
    pyrosim.Send_Joint(name="BLT_BLL", parent="BLT", child="BLL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="BLL", pos=[-0.1, 0.1, 0], size=[0.1, 0.1, 0.5])

    pyrosim.Send_Joint(name="Torso_BRT", parent="Torso", child="BRT", type="revolute", position=".425 -0.1775 1")
    pyrosim.Send_Cube(name="BRT", pos=[-0.1, -0.1, 0], size=[0.15, 0.15, 0.5])
    pyrosim.Send_Joint(name="BRT_BRL", parent="BRT", child="BRL", type="revolute", position="0 0 -0.5")
    pyrosim.Send_Cube(name="BRL", pos=[-0.1, -0.1, 0], size=[0.1, 0.1, 0.5])

    pyrosim.End()

Create_World()
Create_Robot()