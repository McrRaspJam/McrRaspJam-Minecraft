#Load the minecraft API
import api.minecraft as minecraft
import api.block as block

#conect API to the world
mc = minecraft.Minecraft.create()

#Program title
mc.postToChat("Midas Touch V2: Executed")

### Program Content below
#
# Midas Touch V2 - Turns the block below the player into gold
# A block must exist (not air) to be changed into gold
#
###

#get the position of the tile we want to change
tilePos = mc.player.getTilePos()
tilePos.y = tilePos.y - 1

#Ensure not floating
if(mc.getBlock(tilePos.x, tilePos.y, tilePos.z) != block.AIR):
	#set the block at that tile to gold
	mc.setBlock(tilePos.x, tilePos.y, tilePos.z, block.GOLD_BLOCK)
