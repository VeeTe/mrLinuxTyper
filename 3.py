#Works on Python 3.10.6, pynput Version: 1.7.6

import time
import random
import decimal
from pynput.keyboard import Key, Controller
keyboard = Controller()
intKeyAcrc = 92 + random.randrange(6) # 92/100 letters will be typed accurately, 8% will be deleted & retyped
intPermaError = 0 # 0/100 letters will be permanently incorrect
intCharPM = 350 + random.randrange(40) # characters per minute (median is 187 for average human)
#1000 = 681-478 characters a minute
#500 = 330-262 character a minute
#350 = 246 - 187 charcters a minute

intVar = 5+random.randrange(55) # 10% variation for accuracy & CPM


def plsDelay():
	intVariation1 = intCharPM*intVar
	intRandom1 = random.randint(-1*intVariation1, intVariation1)/100
	time.sleep(30/(intCharPM+intRandom1))
	#time.sleep(1)
def plsPress(objPassed):
	plsDelay()
	keyboard.press(objPassed)


def plsRelease(objPassed):
	plsDelay()
	keyboard.release(objPassed)


def plsPressKey(strPassed):
	plsPress(strPassed)
	plsRelease(strPassed)

def plsShiftPK(strPassed):
	plsPress(Key.shift)
	plsPressKey(strPassed)
	plsRelease(Key.shift)

def plsMakeAndFixTypo():
	strAll = "qwertyuiopasdfghjklzxcvbnm`1234567890-=[]\\;',./"
	strRandom1 = strAll[random.randint(0,len(strAll)-1)]
	plsPressKey(strRandom1)
	plsDelay()
	plsPressKey(Key.backspace)

def plsType(strPassed):
	strSC = "~!@#$%^&*()_+{}|:\"<>?" # shift chacater
	strNSC = "`1234567890-=[]\\;',./" #No shift character
	strCap = "QWERTYUIOPASDFGHJKLZXCVBNM"
	strSpecial = "\n\t"
	for int1 in range(len(strPassed)):
		#print(strTypeThis[int1])
		str1 = strPassed[int1]
		#turns upper case into a click
		if random.randint(0,100) > intKeyAcrc: plsMakeAndFixTypo()
		
		if str1.isupper():
			plsShiftPK(str1.lower())
		elif str1 in strSC:
			int1 = strSC.index(str1)
			str2 = strNSC[int1]
			plsShiftPK(str2)
		else:
			plsPressKey(str1)	




str1 = ("KAGW-CD (channel 26) is a low-power, Class A television station in Wichita, Kansas, United States, affiliated with several digital multicast networks, including Cozi TV on its main channel. The station is owned by the Great Plains Television Network, LLC, which also operates low-power Heartland-affiliated station KSMI-LD (channel 30) through a local marketing agreement (LMA) with owner Get After It Media. The two stations share offices on South Greenwood Street in Wichita; KAGW-CD's transmitter is located in rural northwestern Sedgwick County (north-northeast of Colwich)")
intArr1 = []
for int1 in range(5):
	timer1 = time.time()
	plsType(str1)
	print()
	print(time.time()-timer1)
	print(len(str1))
	int2 = 60/((time.time()-timer1)/len(str1))
	intArr1.append(int2)
	print(int2)
int2 = 0
for int1 in intArr1:
	print()
	int2 += int1
	print(int1)
print(int2/len(intArr1))
print(min(intArr1))
print(max(intArr1))

#KAGW-CD (channel 26) is a low-power, Class A te




#time.sleep(99999)

