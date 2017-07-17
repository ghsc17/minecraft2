import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="192.169.44.133", name="yourusername")

# Hint: Instead of thinking of the pyramid as one building, think of every layer of the pyramid as a separate building that is only 1 block high.

block = 24

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x2 = x + 8 #Make it 9 blocks wide.
z2 = z + 8 #Make it 9 blocks long.

mc.setBlocks(x, y, z, x2, y, z2, block)

x = pos.x + 1 #Move over one block in x
y = pos.y + 1 #Move up one block in y
z = pos.z + 1 #move over one block in z

x2 = x + 6 #This will be 7 blocks wide.
z2 = z + 6 #This will be 7 blocks long.

mc.setBlocks(x, y, z, x2, y, z2, block)

x = pos.x + 2
y = pos.y + 2 
z = pos.z + 2

#Keep going!! Can you finish the pyramid? Can you make it hollow?