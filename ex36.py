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
			#print doorA
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
	global doorBContent, doorCContent, doorStates
	if doorAContent == car:
		doorBContent = goat
		doorCContent = goat
		doorStates = 1
	elif doorAContent == goat:
		rand = randint(1, 2)
		if rand == 1:
			doorBContent = car
			doorCContent = goat
			doorStates = 2
		else:
			doorBContent = goat
			doorCContent = car
			doorStates = 3

def printRoomContent():
	print doorAContent, doorBContent, doorCContent

def printAllDoors():
	print doorA, doorB, doorC

def revealOtherDoor():
	print ("Thanks for selecting door %d!") % (doorA)
	print ("I will now show you whats behind one of the other two doors. Are you ready?")
	doorPicker()

def doorPicker():
	#your chosen door, randomly pick one of hte other two doors.
	print("The other two doors that are unopened are door %d and door %d.") % (doorB, doorC)
	#if door 1 is picked, other two doors are 2,3
	#if door 2 is picked, other two doors are 1,3
	#if door 3 is picked, other two doors are 1,2
	if doorStates == 2:
		revelationExplanation(doorC)
	else:
		revelationExplanation(doorB)

def revelationExplanation(doorToOpen):
	print
	print("Well, behind door number %d is a beautiful Goat!") % doorToOpen
	goatImage()
	if doorToOpen == doorC:
		print("Now that you know door %s contains a goat, would you like to switch your door to door number %s?") % (doorC, doorB)
	else:
		#TODO: randomise the doors
		print("Now that you know door %s contains a goat, would you like to switch your door to door number %s?") % (doorB, doorC)

def switchDoor():
	print
	print("Would you like to switch doors?")
	while True: 
		try:
			yes = {'yes','y', 'ye', ''}
			no = {'no','n'}

			choice = raw_input().lower()
			if choice in yes:
   				letsSwitch()
   				break
			elif choice in no:
   				noSwitch()
   				break
			else:
   				print("Please respond with 'yes' or 'no'")
   		except:
   			print("Please respond with 'yes' or 'no'")

def letsSwitch():
	print
	print("So you decided to switch...")
	print
	#now we want to switch doors and reveal whats behind your door
	if doorStates == 1:
		printWinningDoor(True)
	elif doorStates == 2:
		printWinningDoor(True)
	else:
		printWinningDoor(False)
	

def noswitch():
	if doorStates == 3:
		printWinningDoor(True)
	else:
		printWinningDoor(False)

def printWinningDoor(win):
	print """

Lets take a look behind your door...

oh wow...behind your door is a....

	"""
	if win == True:
		carImage()
	else:
		goatImage()

def carImage():
	print"""
	                  _____       _____
     .........   {     }     {     }
    (>>\zzzzzz [======================]
    ( <<<\lllll_\\ _        _____    \\
   _,`-,\<   __#:\\::_    __#:::_:__  \\
  /    . `--,#::::\\:::___#::::/__+_\ _\\
 /  _  .`-    `--,/_~~~~~~~~~~~~~~~~~~~~  -,_
:,// \ .         .  '--,____________   ______`-,
 :: o |.         .  ___ \_____||____\+/     ||~ \
 :;   ;-,_       . ,' _`,""""""""""""""""""""""""\
 \ \_/ _ :`-,_   . ; / \\ ====================== /
  \__/~ /     `-,.; ; o |\___[~~~]_ASCII__[~~~]__:
     ~~~          ; :   ;~ ;  ~~~         ;~~~::;
                   \ \_/ ~/               ::::::;
                    \_/~~/                 \:::/
	"""
def goatImage():
	print"""
                                      ,,~~--___---,
                                     /            .~,
                               /  _,~             )
                              (_-(~)   ~, ),,,(  /'
                               Z6  .~`' ||     \ |
                               /_,/     ||      ||
                         ~~~~~~~~~~~~~~~W`~~~~~~W`~~~~~~~~~
	"""
	#reveal whats behind your door

#Starting Method

def startGame():
	"""
	This starts the game and combines the logic.
	"""
	explainRules()
	doorSelection()
	revealOtherDoor()
	switchDoor()

startGame()