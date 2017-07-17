import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="192.169.44.133", name="yourusername")


user_command = raw_input("Enter command: ")
if user_command == "diamond":
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    diamond_block_id = 56
    mc.setBlock(x, y-1, z, diamond_block_id)
if user_command == "gold":
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    gold_block_id = 14
    mc.setBlock(x, y-1, z, gold_block_id)