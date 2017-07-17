import mcpi.minecraft as minecraft

#NOTE - replace "seanybob" below with your name
mc = minecraft.Minecraft.create(address="192.169.44.133", name="rileyma") 

x = 20000000
y = 50
z = -20000000

mc.player.setPos(x, y, z)

