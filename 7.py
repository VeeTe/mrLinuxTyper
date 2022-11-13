#This class is used for emulating human-like typing to bypass bots restrictions, copy & paste limitations, and manual typing under remote observation (screenshare).


#How to use this class: 
#Create a new document in the same directory as mrLinuxTyper.py
#type the following:
#import mrLinuxTyper.py
#typer1 = mrLinuxTyper()
#typer1.plsType("xd") #Types out xd
#typer1.plsTypeFile("index.html") #Types out a document named index.html (assuming you have one), or modify this parameter to match your requirement
# #run the program & 3 seconds in it will start typing out whatever you've fed it. Hope this helps :)


#Works on Linux, Python 3.10.6, pynput Version: 1.7.6






import time
#Mostly used for creation of timing between """"authentic most definitely human""" key-strokes 

import random
#Used for ML evasion, otherwise if typing consistently at X number of words per minute can eventually get a bot ban

from pynput.keyboard import Key, Controller
keyboard = Controller()
#Used for pressing kys


class mrLinuxTyper():

	def __init__(self, intDelayBeforeTyping1=1, intKeyAcrc1=92, intPermaError=0, intClickSpeed1=350, intVar1=5, intDelayBeforeTyping2=2, intKeyAcrc2=4, intClickSpeed2=40, intVar2=55, strErrorChars="qwertyuiopasdfghjklzxcvbnm`1234567890-=[]\\;',./"):
		#Lol had pre-exiting code here, got lazy & did a bit of a short cut (originally wasn't planning on making this a class)
		self.intDelayBeforeTyping1=intDelayBeforeTyping1
		self.intKeyAcrc1=intKeyAcrc1
		self.intPermaError=intPermaError
		self.intClickSpeed1=intPermaError
		self.intVar1=intVar1
		self.intDelayBeforeTyping2=intDelayBeforeTyping2
		self.intKeyAcrc2=intKeyAcrc2 
		self.intClickSpeed2=intClickSpeed2 
		self.intVar2=intVar2
		self.strErrorChars=strErrorChars
		self.strAll = strErrorChars
		
		
		self.intDelayBeforeTyping = intDelayBeforeTyping1 + random.randrange(self.intDelayBeforeTyping2)
		# Wait before starting to run the typing emulator
		
		self.intKeyAcrc = intKeyAcrc1 + random.randrange(intKeyAcrc2) 
		# 92/100 letters will be typed accurately, 8% will be deleted & retyped
		
		self.intPermaError = intPermaError 
		#0/1000 letters will be permanently incorrect
		
		self.intClickSpeed = intClickSpeed1 + random.randrange(intClickSpeed2) 
		#Keyboard clicks per minute (median character per minute 187 for average human), to avoid getting nae-nae'd by the ML abstain from using more than 300 characters per minute
		#ClickSpeed IS NOT character per minute
		#1000 click speed = 681-478 characters a minute
		#500 = 330-262 character a minute
		#350 = 246 - 187 charcters a minute
		
		self.intVar = intVar1+random.randrange(intVar2) 
		# 10% variation for accuracy & CPM
	def plsDelay(self):
		intVariation1 = self.intClickSpeed*self.intVar
		intRandom1 = random.randint(-1*intVariation1, intVariation1)/100
		time.sleep(30/(self.intClickSpeed+intRandom1))
		#time.sleep(1)
	def plsPress(self, objPassed):
		self.plsDelay()
		keyboard.press(objPassed)


	def plsRelease(self, objPassed):
		self.plsDelay()
		keyboard.release(objPassed)


	def plsPressKey(self, strPassed):
		self.plsPress(strPassed)
		self.plsRelease(strPassed)

	def plsShiftPK(self, strPassed):
		self.plsPress(Key.shift)
		self.plsPressKey(strPassed)
		self.plsRelease(Key.shift)
		
	
	#Makes a typo & fixes it by deleting the typo using backspace (only 1 character typo, but can increase if iterate the commands in this function)
	def plsMakeAndFixTypo(self):
		strRandom1 = self.strAll[random.randint(0,len(self.strAll)-1)]
		self.plsPressKey(strRandom1)
		self.plsDelay()	#Creates a realistic moment of realization that a typo has been made (stellar if getting spectated)
		self.plsPressKey(Key.backspace)
	
	#Makes 1 char typo & does not correct it, stellar for bots when humanity needs to be deplayed
	def plsMakeATypo(self):
		strRandom1 = self.strAll[random.randint(0,len(self.strAll)-1)]
		self.plsPressKey(strRandom1)

	#Goes through logic how the character should be handled then types the string emulating human behavior of typing
	def plsType(self, strPassed):
		strSC = "~!@#$%^&*()_+{}|:\"<>?" # shift chacater
		strNSC = "`1234567890-=[]\\;',./" #No shift character
		strCap = "QWERTYUIOPASDFGHJKLZXCVBNM"
		strSpecial = "\n\t"
		for int1 in range(len(strPassed)):
			#print(strTypeThis[int1])
			str1 = strPassed[int1]
			#turns upper case into a click
			if random.randint(0,100) > self.intKeyAcrc: self.plsMakeAndFixTypo()
			if random.randint(0,1000) > (1000 - self.intPermaError): self.plsMakeATypo()
			if str1.isupper():
				self.plsShiftPK(str1.lower())
			elif str1 in strSC:
				int1 = strSC.index(str1)
				str2 = strNSC[int1]
				self.plsShiftPK(str2)
			elif str1 in strSpecial:
				if str1 == "\n": self.plsPressKey(Key.enter)
				if str1 == "\t": self.plsPressKey(Key.tab)
			else:
				self.plsPressKey(str1)
	
	#Parses a file, then types it out
	def plsTypeFile(self,strPassed):
		openFile = open(strPassed, "r")
		strReturn = ""
		for objLine in openFile:
			strReturn += objLine
		self.plsType(strReturn)


