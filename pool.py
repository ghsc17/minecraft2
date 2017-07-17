import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="192.169.44.133", name="yourusername")

#This will create a solid chunk of whatever block you want.  


pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 10 #11 blocks wide
y2 = y + 5 #6 blocks high
z2 = z + 8 #9 blocks long

block_id = 4

mc.setBlocks(x, y, z, x2, y2, z2, block_id)

#Can you make it hollow?  (hint, the block id for air is 0)

#Can you fill it with water instead?  (hint, the block id for w ter is 9)

#Keep going!!  