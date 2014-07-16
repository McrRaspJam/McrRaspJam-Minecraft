#Load the minecraft API
import api.minecraft as minecraft
import api.block as block

#Load the time library, for delays
import time

#conect API to the world
mc = minecraft.Minecraft.create()

#Give your script a title
mc.postToChat("Fractal: Recursive shapes")

#Uncomment to add a delay before starting
#time.sleep(3)

############ Write your program below #############

###Define the recursive call
def recursive(base, origin, n):
	
	#Simplify base case
	if(n == origin.y):
		#Place a block
		mc.setBlock(origin.x, origin.y, origin.z, block.COBBLESTONE)
		
	else:
		#get the relative height
		height = origin.y - n
		
		#set the boundary x/z values
		xmin = origin.x - height
		xmax = origin.x + height
		zmin = origin.z - height
		zmax = origin.z + height

		#go through each block on that layer
		for x in range(xmin, xmax+1):
			for z in range(zmin, zmax+1):

				#Check if this is a block we wish to change
				if( ((x == xmin) or (x == xmax))
				 or ((z == zmin) or (z == zmax)) ):

					#Set the block
					mc.setBlock(x, n, z, block.COBBLESTONE)

				#Otherwise, the block is inside the pyramid, let's make it gold
				else:#
					#We don't want air to be changed though
					tempBlockId = mc.getBlock(x, n, z)
					if(tempBlockId != 0):
						
						#Set the block
						mc.setBlock(x, n, z, block.GOLD_BLOCK)

	#This layer is finished, call the next one
	if(n > base):
		recursive(base, origin, n-1)


### Main Program below

#get the block the player is stood on
tilePos = mc.player.getTilePos()

#get the low and high point of the pyramid
startBase = tilePos.y - 3
startOrigin = tilePos
startOrigin.y = startOrigin.y + 17

#call the method
recursive(startBase, startOrigin, startOrigin.y)
