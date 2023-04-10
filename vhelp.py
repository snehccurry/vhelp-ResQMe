from Heema import *
from browser import *

root=create_window("vHelp")


left_frame=left_frame(root)
left_frame.pack(ipadx=70)

import os 

print(os.path.exists("disasters\\"))
#img=image(root,path="disasters\\earthquake.png")


def open_weather_frame():
	global x
	x.pack_forget()
	x=BrowserFrame("https://www.msn.com/en-in/weather/forecast/in")
	x.pack(fill=BOTH,expand=True)


def NDMA():
	global x
	x.pack_forget()
	x=BrowserFrame("https://ndma.gov.in/")
	x.pack(fill=BOTH,expand=True)
	pass

import os

def Earthquake():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","earthquake.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
	


def Tsunami():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","Tsunamis.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Hurricane():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","Hurricane.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Tornado():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","tornadoes.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Cyclone():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","cyclone.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Typhoon():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","earthquake.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Flood():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","floods.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Drought():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","drought.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Wildfire():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","wildfires.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Volcanic_eruption():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","volcanoes.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)

def Landslide():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","landslides.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)
def Avalanche():
	global x
	x.pack_forget()
	current_path = os.getcwd()
	earth_quake_file=os.path.join(current_path,"disasters","avalanche.mhtml")
	print(earth_quake_file)
	x=BrowserFrame(earth_quake_file)
	x.pack(fill=BOTH,expand=True)


weather=left_frame_button(left_frame,text="Weather",command=open_weather_frame)
weather.config(font=("calibri",15),pady=5)

NDMA=left_frame_button(left_frame,text="NDMA",command=NDMA)
NDMA.config(font=("calibri",15),pady=5)

Earthquake=left_frame_button(left_frame,text="Earthquake",command=Earthquake)
Earthquake.config(font=("calibri",15),pady=5)


Tsunami=left_frame_button(left_frame,text="Tsunami",command=Tsunami)
Tsunami.config(font=("calibri",15),pady=5)


Hurricane=left_frame_button(left_frame,text="Hurricane",command=Hurricane)
Hurricane.config(font=("calibri",15),pady=5)


Tornado=left_frame_button(left_frame,text="Tornado",command=Tornado)
Tornado.config(font=("calibri",15),pady=5)


Cyclone=left_frame_button(left_frame,text="Cyclone",command=Cyclone)
Cyclone.config(font=("calibri",15),pady=5)


Volcanic_eruption=left_frame_button(left_frame,text="Volcanic Eruption",command=Volcanic_eruption)
Volcanic_eruption.config(font=("calibri",15),pady=5)










Typhoon=left_frame_button(left_frame,text="Typhoon",command=Typhoon)
Typhoon.config(font=("calibri",15),pady=5)


Flood=left_frame_button(left_frame,text="Flood",command=Flood)
Flood.config(font=("calibri",15),pady=5)


Drought=left_frame_button(left_frame,text="Drought",command=Drought)
Drought.config(font=("calibri",15),pady=5)


Wildfire=left_frame_button(left_frame,text="Wildfire",command=Wildfire)
Wildfire.config(font=("calibri",15),pady=5)




Avalanche=left_frame_button(left_frame,text="Avalanche",command=Avalanche)
Avalanche.config(font=("calibri",15),pady=5)


Landslide=left_frame_button(left_frame,text="Landslide",command=Landslide)
Landslide.config(font=("calibri",15),pady=5)









x=BrowserFrame("https://www.msn.com/en-in/weather/forecast/in")
x.pack(fill=BOTH,expand=True)
root.mainloop()