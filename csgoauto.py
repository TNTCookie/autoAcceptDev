import win32api, win32con, os, time

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

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