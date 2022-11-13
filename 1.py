#Works on Python 3.10.6, pynput Version: 1.7.6

import time
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()



# Press and release space
#keyboard.press(Key.ctrl)
#keyboard.press(Key.shift)
#keyboard.press("c")
#keyboard.release("c")
#keyboard.release(Key.shift)
#keyboard.release(Key.space)


intKeyAcrc = 92 # 92/100 letters will be typed accurately, 8% will be deleted & retyped
intPermaError = 0 # 0/100 letters will be permanently incorrect
intCharPM = 50#220 # characters per minute (median is 187 for average human)
intVar = 10 # 10% variation for accuracy & CPM

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
#keyboard.press('a')
#keyboard.release('a')

# Type two upper case As
#keyboard.press('A')
#keyboard.release('A')
#with keyboard.pressed(Key.shift):
#    keyboard.press('a')
#    keyboard.release('a')

# Type 'Hello World' using the shortcut type method
#keyboard.type('Hello World')


def plsDelay():
	intVariation1 = intCharPM*intVar/100
	intRandom1 = random.randint(-1*intVariation1, intVariation1)
	time.sleep(1/(intCharPM+intRandom1))
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



strSC = "~!@#$%^&*()_+{}|:\"<>?" # shift chacater
strNSC = "`1234567890-=[]\\;',./" #No shift character
strCap = "QWERTYUIOPASDFGHJKLZXCVBNM"
strAll = "qwertyuiopasdfghjklzxcvbnm" + strNSC
strTypeThis = "afldjasdflSfasdf34823*'\""
def plsMakeAndFixTypo():
	
	strRandom1 = strAll[random.randint(0,len(strAll)-1)]
	plsPressKey(strRandom1)
	time.sleep(1)
	plsPressKey(Key.backspace)
#afffllldjjjaaasdffflllSfasssdddf3334823***'"
	
	
	
time.sleep(2)	
for int1 in range(len(strTypeThis)):
	#print(strTypeThis[int1])
	str1 = strTypeThis[int1]
	#turns upper case into a click		
	if str1.isupper():
		plsShiftPK(str1.lower())
	elif str1 in strSC:
		int1 = strSC.index(str1)
		str2 = strNSC[int1]
		plsShiftPK(str2)
	
	else:
		plsPressKey(str1)
		

time.sleep(3)
