import win32api, win32con, os, time
from win32gui import GetWindowText, GetForegroundWindow

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def dota():
	timer = 0
	window = (GetWindowText(GetForegroundWindow()))
	print("Checking For Game, Current Window is '" + window + "'")
	
	while timer == 0:
		while GetWindowText(GetForegroundWindow()) != "Dota 2": #check repeater
			if GetWindowText(GetForegroundWindow()) != window and GetWindowText(GetForegroundWindow()) != "": #checks if changed
				print("Checking For Game, Current Window is '" + (GetWindowText(GetForegroundWindow())) + "'")
			window = (GetWindowText(GetForegroundWindow()))
	
		#after while is finished checks if its dota
		print("Found Game")
		print("Checking if its Q")
		time.sleep(3)
		if GetWindowText(GetForegroundWindow()) == "Dota 2":
			timer = 1
		print("Was not Q whoops")
	

	print("Game Found")		
	click (954,522)
	print("Job done")
	print("Clicked at" + win32api.GetCursorPos())
	print("Press any key to close app")
	os.system('pause')
	
def csgo():
	def get_pixel_colour(i_x, i_y): #gets the color of a pixel
		import win32gui
		i_desktop_window_id = win32gui.GetDesktopWindow()
		i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
		long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
		i_colour = int(long_colour)
		return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

	def getColorPos(): #returns color of cursor pixel
		pos = win32api.GetCursorPos()
		color = get_pixel_colour(pos[0], pos[1])
		return color

	def getColor(): #gets color of button
		pos1 = 491
		pos2 = 255
		color = get_pixel_colour(pos1, pos2)
		return color

	while getColor() != (255, 255, 255): #checks if color is white
		print("Waiting...")

	print("Found Match") 
	time.sleep(1)
	print("Clicking")
	click(491, 255)

def askForRepeat():
	answer = raw_input("Repeat?\n")
	if answer == "yes" or answer == "y":
		print "OK"
	else:
		global repeat
		repeat = True

def askGame():
	s = True
	while s == True:
		game = raw_input("What game: CS or Dota?\n")
		game = game.lower()
		
		if game == "csgo" or game == "cs":
			csgo()
			s = False
			askForRepeat()
		elif game == "dota" or game == "d":
			dota()
			s = False
			askForRepeat()
		else:
			print("Try again m8, CS or Dota?\n")
		
repeat = False
while repeat == False:
	askGame()