import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
length,width,height = 1,1,1
x,y,z = 0,0,0.5
#pyrosim.Send_Cube(name="Box", pos=[x,y,z], size = [length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[x+5,y,z], size = [length,width,height])
for j in range(0,10):
    for i in range(0,10):
        pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
        z = z + 1
        length, width, height = length*0.9,width*0.9,height*0.9
    x = x + 5
pyrosim.End()