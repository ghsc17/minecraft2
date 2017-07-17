import mcpi.minecraft as minecraft
import time

server_address = "192.169.44.133"
my_player_name = "username"  #your username

mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)

my_id = mc.getPlayerEntityId(my_player_name)

print("Script started! Type in your commands in Minecraft chat to activate. Hit command (or control) + C in your terminal to stop.")

while True:

    for chatpost in mc.events.pollChatPosts():
    
        if chatpost.entityId == my_id:

            if chatpost.message.lower() == "hi":
                mc.postToChat("Hello right back at you!")

            if chatpost.message.lower() == "where am i":
                my_pos = mc.player.getPos()
                mc.postToChat(my_player_name + " is at " + str(my_pos))
                
            if chatpost.message.lower() == "go home":
                x = 52
                y = 52
                z = -57
                
                mc.player.setPos(x, y, z)

            if "make building" in chatpost.message.lower():
                pos = mc.player.getPos()
                x = pos.x
                y = pos.y
                z = pos.z
                
                x2 = x + 8
                y2 = y + 5
                z2 = z + 8
                
                block_id = 4
                
                mc.setBlocks(x, y, z, x2, y2, z2, block_id)
                
            if "my new command" in chatpost.message.lower():
                mc.postToChat("This is where my code for my new command will go")
                
                
                
    time.sleep(.1)