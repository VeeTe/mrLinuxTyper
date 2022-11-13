#Works on Python 3.10.6, pynput Version: 1.7.6

import time
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()

class mrLinuxTyper():
	def __init__(self, intDelayBeforeTyping1=1, intKeyAcrc1=92, intPermaError=0, intClickSpeed1=350, intVar1=5, intDelayBeforeTyping2=2, intKeyAcrc2=4, intClickSpeed2=40, intVar2=55, strErrorChars="qwertyuiopasdfghjklzxcvbnm`1234567890-=[]\\;',./"):
		self.strAll = strErrorChars
		self.intDelayBeforeTyping = self.intDelayBeforeTyping1 + random.randrange(self.intDelayBeforeTyping2)

		self.intKeyAcrc = intKeyAcrc1 + random.randrange(intKeyAcrc2) 
		# 92/100 letters will be typed accurately, 8% will be deleted & retyped
		
		self.intPermaError = intPermaError #0/1000 letters will be permanently incorrect
		
		self.intClickSpeed = intClickSpeed1 + random.randrange(intClickSpeed2) 
		# characters per minute (median is 187 for average human)
		#1000 = 681-478 characters a minute
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
		plsDelay()
		keyboard.press(objPassed)


	def plsRelease(self, objPassed):
		plsDelay()
		keyboard.release(objPassed)


	def plsPressKey(self, strPassed):
		plsPress(strPassed)
		plsRelease(strPassed)

	def plsShiftPK(self, strPassed):
		plsPress(Key.shift)
		plsPressKey(strPassed)
		plsRelease(Key.shift)
	def plsMakeAndFixTypo(self):
		strRandom1 = strAll[random.randint(0,len(self.strAll)-1)]
		plsPressKey(strRandom1)
		plsDelay()
		plsPressKey(Key.backspace)
		
	def plsMakeATypo(self):
		strRandom1 = strAll[random.randint(0,len(self.strAll)-1)]
		plsPressKey(strRandom1)


	def plsType(self, strPassed):
		strSC = "~!@#$%^&*()_+{}|:\"<>?" # shift chacater
		strNSC = "`1234567890-=[]\\;',./" #No shift character
		strCap = "QWERTYUIOPASDFGHJKLZXCVBNM"
		strSpecial = "\n\t"
		for int1 in range(len(strPassed)):
			#print(strTypeThis[int1])
			str1 = strPassed[int1]
			#turns upper case into a click
			if random.randint(0,100) > self.intKeyAcrc: plsMakeAndFixTypo()
			if random.randint(0,1000) > (1000 - self.intPermaError): plsMakeATypo()
			if str1.isupper():
				plsShiftPK(str1.lower())
			elif str1 in strSC:
				int1 = strSC.index(str1)
				str2 = strNSC[int1]
				plsShiftPK(str2)
			elif str1 in strSpecial:
				if str1 == "\n": plsPressKey(Key.enter)
				if str1 == "\t": plsPressKey(Key.tab)
			else:
				plsPressKey(str1)	

	def plsParseFile(strPassed):
		openFile = open(strPassed, "r")
		strReturn = ""
		for objLine in openFile:
			strReturn += objLine
		return strReturn

typer1 = mrLinuxTyper()
typer1.plsType("xd")
