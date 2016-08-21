import win32api, win32con, os, time
from win32gui import GetWindowText, GetForegroundWindow

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

timer = 0
window = (GetWindowText(GetForegroundWindow()))
print("Checking For Game, Current Window is '" + window + "'")

while timer == 0:
	while GetWindowText(GetForegroundWindow()) != "Dota 2": #check repeater
	#	newWindow = (GetWindowText(GetForegroundWindow()))
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
	

print ("Game Found")
time.sleep(1)		
click (957,581)
os.system('pause')


