import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="192.169.44.133", name="yourusername")

while True:

    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    
    block = 38
    mc.setBlock(x, y, z, block)
    
    time.sleep(0.1)

#What else can we do?

#Can you 