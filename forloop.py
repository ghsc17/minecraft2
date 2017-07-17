import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="192.169.44.133", name="yourusername")


for i in range(5):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + ?
    y2 = y
    z2 = z + ?
    mc.setBlocks(x, y, z, x2, y2, z2, block)
    
    