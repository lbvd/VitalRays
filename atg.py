#!/usr/bin/python3
#gui application
#upgrade of at.py
#contact me via E-Mail: lbvd@protonmail.com
#

import tkinter
import time
import subprocess as sp

place = False
countfc = 0
shellco = False
shellti = 0
def options():
	global place
	place = True
	global shellco
	def op1():
		global shellco
		shellco = "shutdown now"
		lbco["text"] = "entered command: "+shellco

	def op2():
		global shellco
		shellco = "reboot"
		lbco["text"] = "entered command: "+shellco

	def op3():
		global shellco
		shellco = "init 3"
		lbco["text"] = "entered command: "+shellco

	def op4():
		global shellco
		shellco = "pm-suspend"
		lbco["text"] = "entered command: "+shellco

	def op5():
		global shellco
		shellco = "killall -o 1"
		lbco["text"] = "entered command: "+shellco

	def op6():
		global shellco
		shellco = "sudo apt-get update && apt-get full-upgrade"
		lbco["text"] = "entered command: "+shellco+" a password is required"

	def opclose():
		btop1.destroy()
		btop2.destroy()
		btop3.destroy()
		btop4.destroy()
		btop5.destroy()
		btop6.destroy()
		btop7.destroy()

	#enco.destroy()
	btop1 = tkinter.Button(fr1, text = "shutdown", command = op1)
	btop2 = tkinter.Button(fr1, text = "reboot(to boot windows)", command = op2)
	btop3 = tkinter.Button(fr1, text = "save mode (run level 3)", command = op3)
	btop4 = tkinter.Button(fr1, text = "standby", command = op4)
	btop5 = tkinter.Button(fr1, text = "clean up (stop unnessesary processes)", command = op5)
	btop6 = tkinter.Button(fr1, text = "update and upgrade the system (via apt)", command = op6)
	btop7 = tkinter.Button(fr1, text = "close options", command = opclose)
	btop1.pack(side = "left")
	btop2.pack(side = "left")
	btop3.pack(side = "left")
	btop4.pack(side = "left")
	btop5.pack(side = "left")
	btop6.pack(side = "left")
	btop7.pack(side = 'left')



#def canc():
#	sp.run()

def start():
	sec = shellti * 60
	sec = int(sec)
	lbinf["text"] = "in "+str(sec)+" minutes, the command: "+str(shellco)+" will be executed"
	time.sleep(sec)
	sp.run(shellco, shell = True)

def co():
	countfc =+ 1
	global shellco
	if place == False:
		shellco = enco.get()
		lbco["text"] = "entered command: "+shellco
	if place == True:
		shellco = str(shellco)

def ti():
	countfc =+ 1
	global shellti
	tim = enti.get()
	try:
		shellti = float(tim)
		lbti["text"] = "entered time: "+tim+" minutes"
	except:
		lbti["text"] = "only numbers, try it again"


#GUI (tkinter preparation)
def gui():
	global fr0, fr1, fr2, lbco, enco, btco1, btco2, lbti, enti, btti, main, lbinf
	main = tkinter.Tk()

	fr0 = tkinter.Frame(main)
	fr1 = tkinter.Frame(main, relief = "groove", borderwidth = 5)
	fr2 = tkinter.Frame(main, relief = "groove", borderwidth = 5)
	fr0.pack()
	fr1.pack(padx = 19, pady =17)
	fr2.pack(padx = 19, pady =17)

	lbinf = tkinter.Label(fr0, text = "give arguments otherwise the default arguments will be executed")
	lbinf.pack()
	btst = tkinter.Button(fr0, text = "R U N", command = start)
	btst.pack()


	lbco = tkinter.Label(fr1, text = "enter command(default: shutdown)")
	lbco.pack()
	enco = tkinter.Entry(fr1)
	enco.pack()
	btco1 = tkinter.Button(fr1, text = "Enter", command = co)
	btco2 = tkinter.Button(fr1, text = "options", command = options)
	btco1.pack()
	btco2.pack()

	lbti = tkinter.Label(fr2, text = "enter time in minutes ")
	lbti.pack()
	enti = tkinter.Entry(fr2)
	enti.pack()
	btti = tkinter.Button(fr2, text = "Enter", command = ti)
	btti.pack()

	main.mainloop()
