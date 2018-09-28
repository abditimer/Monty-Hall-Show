from random import randint
'''
startGame(
	explainIntro()
	doorSelection()
	revelDoors()
	switchOptions()
	reveal()
)
'''

#Methods

def explainRules():
	"""
	This method introduces the game to the user.
	This has no logic, just text printed out.
	"""
	print """
My name is Abdi, and welcome to the Monty Hall Shooooooow!

This show is intended to teach you about the famous monty hall problem!

Well, there's no time to waste, lets get right into it!

 ---     ---     ---        
|   |   |   |   |   |      
|  -|   |  -|   |  -|      
|   |   |   |   |   |      
 ---     ---     ---          
  1       2       3     

Behind one of the doors above, is a BRAND NEW CAR!

Unfortunately, behind the other 2 doors, there are some goats!

So, how lucky do you feel?

	"""

def doorSelection():
	print ("What door do you want to select?")
	doorSelectionHandler()

	
def doorSelectionHandler():
	global doorA
	while True:
		try:
			doorA = int(input(">"))
			print doorA
			if doorA <= 3 and doorA >=1:
				break
			else:
				print("Please choose a door from one of the above!")
		except:
			print("Please choose a door!")
	setOtherDoors()
	setRoomContents()

def setDoorNumbers(door2New, door3New):
	global doorB, doorC
	doorB = door2New
	doorC = door3New

def setOtherDoors():
	"""
	This method sets the door you selected and other doors to global variables.
	"""
	if doorA == 1:
		setDoorNumbers(2, 3)
	elif doorA == 2:
		setDoorNumbers(1,3)
	else:
		setDoorNumbers(1,2)
	#printAllDoors()

def setRoomContents():
	global doorAContent
	global car, goat
	car = "Car"
	goat = "Goat"
	rand = randint(1, 3)
	if rand == 1:
		doorAContent = car
	else:
		doorAContent = goat
	setOtherRoomContents()
	

def setOtherRoomContents():
	global doorBContent, doorCContent
	if doorAContent == car:
		doorBContent = goat
		doorCContent = goat
	elif doorAContent == goat:
		rand = randint(1, 2)
		if rand == 1:
			doorBContent = car
			doorCContent = goat
		else:
			doorBContent = goat
			doorCContent = car

def printRoomContent():
	print doorAContent, doorBContent, doorCContent

def printAllDoors():
	print doorA, doorB, doorC

def revealOtherDoor():
	print ("Thanks for selecting door %d!") % (doorA)



#Starting Method

def startGame():
	"""
	This starts the game and combines the logic.
	"""
	explainRules()
	doorSelection()
	revealOtherDoor()


startGame()