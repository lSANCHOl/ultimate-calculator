#!/bin/python3
#Denary, Binary, Hexadecimal number calculator
import sys
import os
import math
import collections

print("""
######################################################################################
################### THE ULTIMATE CALCULATOR made by lSANCHOl #########################
###################################################################################### 

CALCULATIONS:				  CONVERSIONS:
________________________________________   ___________________________________________
|normal calculator           |  calc   |  |denary -> binary           |    den2bin   |
|SpeedDistanceTime           |  std    |  |binary -> denary           |    bin2den   |
|square root                 |  root   |  |denary -> hexadecimal      |    den2hex   |
|power of                    |  power  |  |hexadecimal -> denary      |    hex2den   |
|quadratic                   |  quad   |  |binary -> hexadecimal      |    bin2hex   |
|pythagoras                  |  pyth   |  |hexadecimal -> binary      |    hex2bin   |
|fibonacci sequence          |  fibo   |  |centimetres -> inches      |    cm2inch   |
|Mean, Mode, Median, Range   |  mmm    |  |inches -> centimetres      |    inch2cm   |
|Cosine & Sine rule	     |  cosi   |  |miles -> kilometres        |    mile2km   |
''''''''''''''''''''''''''''''''''''''''  |kilometres -> miles        |    km2mile   |
                                          |feet -> metres             |    feet2m    |
					  |metres -> feet             |    m2feet    |
                                          |feet and inches -> metres  |  feetinch2m  |
                                          ''''''''''''''''''''''''''''''''''''''''''''
Choose a calculation or conversion by entering one of the commands
Type 'help' anywhere to see instructions on modules
Type 'exit' anywhere to return to here
Type 'back' to go back within a module
""")


choice = input("Ultimate-Calculator#>")

if choice == "exit":
	sys.exit()

print("="*60)





def SineCosRule():
	
	pick = "f"
	pick = input("Sin & Cos Rule#>")
	if pick == "help":
		pick = input("""
Options:
_____________________________
Sine rule for sides    | ss |
Sine rule for angles   | sa |
Cosine rule for sides  | cs |
Cosine rule for angles | ca |
-----------------------------
[type 'exit' to go back]""")

	if pick == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	

	#working
	while pick == "ss":
		print("""
Sine rule for sides Instructions:
+ A is opposite the side you are working out
+ b is the given side
+ B is opposite b
[type 'exit' to go back]""")
		print('\n')
		A = 0
		b = 0
		B = 0
		A = input("A: ")
		if str(A) == "exit":
			break
			SineCosRule()
			
		b = input("b: ")
		if str(b) == "exit":
			break
			SineCosRule()
		B = input("B: ")
		if str(B) == "exit":
			break
			SineCosRule()		
	
		else:	
			rA = math.radians(float(A))
			rB = math.radians(float(B))
			sinea = math.sin(rA)
			sineB = math.sin(rB)
			tmp = sinea * float(b)
			
			x = tmp / sineB 
			print(x)
		


	#working
	while pick == "sa":
		print("""
Sine rule for angles Instructions:
+ a is the given side
+ A is the angle opposite a
+ b is opposite the angle you are working out
[type 'exit' to go back]""")

		print('\n')
		a = 0
		A = 0
		b = 0
		a = float(input("a: "))
		if str(a) == "exit":
			break
			SineCosRule()
		A = float(input("A: "))
		if str(A) == "exit":
			break
			SineCosRule()
		b = float(input("b: "))
		if str(b) == "b":
			break
			SineCosRule()
		else:	
			rA = math.radians(float(A))
			sinA = math.sin(rA)
			ba = float(b) / float(a)
			tmp = sinA * ba
			tmp1 = math.asin(tmp)
			tmp2 = math.degrees(tmp1)
			print(tmp2)



	#working
	while pick == "cs":
		print("""
Cosine rule for sides Instructions:
+ a and b are interchangeable sides
+ C is the angle opposite the side you are working out
[type 'exit' to go back]""")
		print('\n')
		a = 0
		b = 0
		c = 0
		a = input("a: ")
		if str(a) == "exit":
			break
			SineCosRule()
		b = input("b: ")
		if str(b) == "exit":
			break
			SineCosRule()
		C = input("C: ")	
		if str(C) == "exit":
			break
			SineCosRule()
		
		else:
			a2b2 = (float(a) ** 2) + ( float(b) ** 2)
			rC = math.radians(float(C))
			cosC = math.cos(rC)
			ab2cosC = (2 * float(a) * float(b)) * (cosC)
			tmp = float(a2b2) - float(ab2cosC)
			tmp1 = tmp ** 0.5
			print(tmp1)
		
		
		
	#working
	while pick == "ca":
		print("""
Cosine rule for angles Instructions:
+ a is always opposite the angle you are working out
+ b and c are interchangeable
[type 'exit' to go back]""")
		print('\n')
		a = 0
		b = 0
		c = 0
		a = input("a: ")
		if str(a) == "exit":
			break
			SineCosRule()	
		b = input("b: ")
		if str(b) == "exit":
			break
			SineCosRule()
		c = input("c: ")
		if str(c) == "exit":
			break
			SineCosRule()
		else:
			a2 = float(a) ** 2
			b2 = float(b) ** 2
			c2 = float(c) ** 2
			tmp1 = b2 + c2 - a2
			tmp = 2 * float(b) * float(c)
			cosA = tmp1 / tmp
			ans = math.acos(cosA)
			ans1 = math.degrees(ans)
			print(ans1)
		
	
if choice == "cosi":
	run = True
	while run == True:
		SineCosRule()



def MeanModeMedian():
	
	
	nums = input("input all numbers with a space inbetween each of them: ")
	if nums == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	print("="*60)
	numbers = nums.split()
	numbers = [int(i) for i in numbers]
	len1 = len(numbers)
	total = 0
	mode = 0
	
	numbers.sort()
	print("Numbers: ", numbers)
	for i in range (len1):
		total += int(numbers[i])
		mean = float(total) / len1
	print("Mean:",mean)
	
	
				
	data = collections.Counter(numbers)
	data_list = dict(data)
	max_value = max(list(data.values()))
	mode_val = [num1 for num1, freq in data_list.items() if freq == max_value]
	if len(mode_val) == len(numbers):
   		print("Mode: No mode")
	else:
   		print("Mode: " + ', '.join(map(str, mode_val)))
   	
	
	if len(numbers) % 2 == 0:
   		first_median = numbers[len(numbers) // 2]
   		second_median = numbers[len(numbers) // 2 - 1]
   		median = (first_median + second_median) / 2
	else:
		median = numbers[len(numbers) // 2]
	print("Median:",median)
	
	ran = int(numbers[-1]) - int(numbers[0])
	print("Range:",ran)
	print("Sum:",total)
	print("Count:",len(numbers))
	print("="*60)
				
				
		
	
if choice == "mmm":
	run = True
	while run == True:
		MeanModeMedian()

def fibonacci():
	series = [0, 1]
	length = input("how far into the fibonacci sequence do you want to go?: ")
	if length == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	if length == 1:
		print("[0]")
	if length == 2:
		print("[0, 1]")

	length = int(length) - 2
	
	while length >= 1:	
		for i in range (length):
			tmp = series[i] + series[i+1]
			series.append(tmp)
		choose = input("print all numbers in sequence or the just the number chosen? [all/chosen]:") 
		if choose == "all":
			print(series)
		if choose == "chosen":
			print (series[-1])
		if choose == "exit":
			os.execl(sys.executable, sys.executable, *sys.argv)
		if choose == "back":
			fibonacci()
		break
	print("="*45)
if choice == "fibo":
	run = True
	while run == True:
		fibonacci()

def den2bin():
	denary = input("please input a denary number: ")	
	if denary == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	binary = bin(int(denary))
	binary = str(binary)
	print("="*45)	
	print("Result: ",binary[2:])
	print("="*45)	
if choice == "den2bin":	
	run = True
	while run == True:
		den2bin()
	

def bin2den():
	binary = input("please input a binary number: ")
	if binary == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	ans = int(binary, 2)
	print("="*45)	
	print("Result:",ans)
	print("="*45)	
if choice == "bin2den":	
	run = True
	while run == True:
		bin2den()
	

def den2hex():
	denary = input("please input a denary number: ")
	if denary == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	hexadecimal = hex(int(denary))
	print("="*45)	
	print("Result:",hexadecimal[2:])
	print("="*45)	
if choice == "den2hex":	
	run = True
	while run == True:
		den2hex()
	
def hex2den():
	hexinput = input("please input a hexadecimal number: ")
	if hexinput == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
		
	hexadecimal = int(hexinput, 16)
	print("="*45)	
	print("Result:",hexadecimal)
	print("="*45)	
if choice == "hex2den":	
	run = True
	while run == True:
		hex2den()
	
def bin2hex():
	binary = input("please input a binary number: ")
	if binary == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	binary1 = int(binary, 2)
	hexadecimal = hex(binary1)
	print("="*45)
	print("Result:",hexadecimal[2:])
	print("="*45)	
if choice == "bin2hex":
	run = True
	while run == True:
		bin2hex()
	
def hex2bin():
	hexinput = input("please input a hexidecimal number: ")
	if hexinput == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	hexadecimal = int(hexinput, 16)
	binary = bin(hexadecimal)
	print("="*45)	
	print("Result:",binary[2:])
	print("="*45)	
if choice == "hex2bin":	
	run = True
	while run == True:
		hex2bin()

def calculator():
	print("REMEMBER * = times and / = divide")	
	print("your format should look like this: 1 + 1")	
	Input = input("input your calcution: ")
	if Input == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
		
	tmp = Input.split()
	tmp1 = (tmp[0])
	tmp2 = (tmp[1])
	tmp3 = (tmp[2])
	if tmp2 == "+":
		result = float(tmp1)+float(tmp3)
	elif tmp2 == "-":
		result = float(tmp1)-float(tmp3)
	elif tmp2 == "/":
		result = float(tmp1)/float(tmp3)
	elif tmp2 == "*":
		result = float(tmp1)*float(tmp3)
	print("="*45)	
	print(result)
	print("="*45)
if choice == "calc":
	run = True
	while run == True:
		calculator()

def cm2inch():
	inp = input("input the amount of centimetres: ")
	if inp == "exit":	
		os.execl(sys.executable, sys.executable, *sys.argv)
	result = float(inp) / 2.54
	print("="*45)	
	print(result,"inches")
	print("="*45)
if choice == "cm2inch":
	run = True
	while run == True:
		cm2inch()

def inch2cm():
	inp = input("input the amount of inches: ")
	if inp == "exit":	
		os.execl(sys.executable, sys.executable, *sys.argv)
	result = float(inp) * 2.54
	print(45*"=")	
	print(result,"cm")
	print("="*45)
if choice == "inch2cm":
	run = True
	while run == True:
		inch2cm()

def mile2km():
	inp = input("input the amount of miles: ")
	if inp == "exit":	
		os.execl(sys.executable, sys.executable, *sys.argv)
	result = float(inp) * 1.609
	print(45*"=")	
	print(result,"km")
	print("="*45)
if choice == "mile2km":
	run = True
	while run == True:
		mile2km()

def km2mile():
	inp = input("input the amount of kilometres: ")
	if inp == "exit":	
		os.execl(sys.executable, sys.executable, *sys.argv)
	result = float(inp) / 1.609
	print(45*"=")	
	print(result,"miles")
	print("="*45)
if choice == "km2mile":
	run = True
	while run == True:
		km2mile()

def power():
	print("the format shoud look like this 2 8")	
	inp = input("please input here: ")
	if inp == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	tmp = inp.split()
	tmp1 = (tmp[0])
	tmp2 = (tmp[1])
	result = float(tmp1)**float(tmp2)
	print(45*"=")	
	print(result)
	print("="*45)
if choice == "power":
	run = True
	while run == True:
		power()

def feet2m():
	inp = input("please input amount of feet: ")
	if inp == "exit":	
		os.execl(sys.executable, sys.executable, *sys.argv)
	result = float(inp) / 3.281
	print("="*45)
	print(result,"m")
	print("="*45)
if choice == "feet2m":
	run = True
	while run == True:
		feet2m()

def m2feet():
	inp = input("please input amount of metres: ")
	if inp == "exit":	
		os.execl(sys.executable, sys.executable, *sys.argv)
	result = float(inp) * 3.281
	print("="*45)
	print(result,"feet")
	print("="*45)
if choice == "m2feet":
	run = True
	while run == True:
		m2feet()


def feetinch2m():
	print("the format is: feet inch")
	inp = input("input feet and inches: ")
	if inp == "exit":	
		os.execl(sys.executable, sys.executable, *sys.argv)
	tmp = inp.split()
	feet = float(tmp[0])
	inch = float(tmp[1])
	fmetres = feet / 3.281
	imetres = inch * 2.54
	imetres = imetres / 100
	metres = imetres + fmetres
	print("="*45)
	print(metres,"m")
	print("="*45)
if choice == "feetinch2m":
	run = True
	while run == True:
		feetinch2m()

def root():
	inp = input("input a number: ")
	if inp == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	result = math.sqrt(float(inp))
	print(result)
if choice == "root":
	run = True
	while run == True:
		root()
	


def quadratic():
	a = input("a: ")
	if a == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	b = input("b: ")
	if b == "back":
		a = input("a: ")
		if a == "exit":
			os.execl(sys.executable, sys.executable, *sys.argv)
		b = input("b: ")
	if b == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	c = input("c: ")
	if c == "back":
		b = input("b: ")
		if b == "exit":
				os.execl(sys.executable, sys.executable, *sys.argv)
		if b == "back":
			a = input("a: ")
			if a == "exit":
				os.execl(sys.executable, sys.executable, *sys.argv)
			b = input("b: ")
			if b == "exit":
				os.execl(sys.executable, sys.executable, *sys.argv)
		c = input("c: ")
		if c == "back":
			b = input("b: ")
			c = input("c: ")	
	if c == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)


	b1 = float(b) - float(b) - float(b)

	bsqr = float(b) ** 2
	sqrt = float(bsqr) - 4 * float(a) * float(c)
	sqrt1 = float(sqrt) ** 0.5


	x1 = complex(b1) + complex(sqrt1)
	x2 = 2 * float(a)

	x3 = complex(b1) - complex(sqrt1)
	x4 = 2 * float(a)

	x_p = complex(x1) / complex(x2)
	x_n = complex(x3) / complex(x4)


	print("X = ",x_p)
	print("-X = ",x_n)
	print("="*45)
if choice == "quad":
	run = True 
	while run == True:
		quadratic()

def pythagoras():
	print("a^2 x b^2 = c^2")
	print("for unkown value enter \"?\"")
	a = input("Value of a: ")
	if a == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	b = input("Value of b: ")
	if b == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	if b == "back":
		a = input("Value of a: ")
		if a == "exit":
			os.execl(sys.executable, sys.executable, *sys.argv)
		b = input("Value of b: ")
		if b == "exit":
			os.execl(sys.executable, sys.executable, *sys.argv)
			
	c = input("Value of c: ")
	if c == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	if c == "back":
		b = input("Value of b: ")
		if b == "exit":
			os.execl(sys.executable, sys.executable, *sys.argv)
		if b == "back":
			a = input("Value of a: ")
			if a == "exit":
				os.execl(sys.executable, sys.executable, *sys.argv)
			b = input("Value of b: ")
			if b == "exit":
				os.execl(sys.executable, sys.executable, *sys.argv)
			
				
		c = input("Value of c: ")
		if c == "exit":
			os.execl(sys.executable, sys.executable, *sys.argv)
				
	
		
		
	
	if c == "?":
		tmp = (float(a)**2) + (float(b)**2)
		tmp1 = (float(tmp)**0.5)
		print("Value of c: ", tmp1)
	if a == "?":
		tmp = (float(c)**2) - (float(b)**2)
		tmp1 = (float(tmp)**0.5)
		print("Value of a: ", tmp1)
	if b == "?":
		tmp = (float(c)**2) - (float(a)**2)
		tmp1 = (float(tmp)**0.5)
		print("Value of b: ", tmp1)
	print("="*45)
if choice =="pyth":
	run = True
	while run == True:
		pythagoras()
	
def SpeedDistanceTime():	
	
		
	s = input("Distance(s): ")
	if s == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	v = input("Speed(v): ")
	if v == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	if v == "back":
		s = input("Distance(s): ")
		v = input("Speed(v): ")
	t = input("Time(t): ")
	if t == "exit":
		os.execl(sys.executable, sys.executable, *sys.argv)
	
	if t == "back":
		v = input("Speed(v): ")
		t = input("Time(t): ")
	print("Distance:",s,"  Speed:",v, "  Time:",t)
#distance
	if v[-3:] == "kph" and t[-1:] == "h" and s == "?km":
		v1 = v[:-3]
		t1 = t[:-1]
		s = float(v1) * float(t1)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "kph" and t[-1:] == "m" and s == "?km":
		v1 = v[:-3]
		t1 = t[:-1]
		t2 = float(t1) / 60
		s = float(v1) * float(t2)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "kph" and t[-1:] == "s" and s == "?km":
		v1 = v[:-3]
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "mps" and t[-1:] == "s" and s == "?km":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "mps" and t[-1:] == "h" and s == "?km":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		s = float(v1) * float(t1)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "mps" and t[-1:] == "m" and s == "?km":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		t1 = float(t1) / 60
		s = float(v1) * float(t1)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "mph" and t[-1:] == "h" and s == "?km":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		s = float(v1) * float(t1)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "mph" and t[-1:] == "m" and s == "?km":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		t1 = float(t1) / 60
		s = float(v1) * float(t1)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "mph" and t[-1:] == "s" and s == "?km":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		print("Distance(s):",s,"km")
	
	if v[-3:] == "kph" and t[-1:] == "h" and s == "?m":
		v1 = v[:-3]
		t1 = t[:-1]
		s = float(v1) * float(t1)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "kph" and t[-1:] == "m" and s == "?m":
		v1 = v[:-3]
		t1 = t[:-1]
		t2 = float(t1) / 60
		s = float(v1) * float(t2)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "kph" and t[-1:] == "s" and s == "?m":
		v1 = v[:-3]
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "mps" and t[-1:] == "s" and s == "?m":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "mps" and t[-1:] == "h" and s == "?m":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		s = float(v1) * float(t1)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "mps" and t[-1:] == "m" and s == "?m":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		t1 = float(t1) / 60
		s = float(v1) * float(t1)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "mph" and t[-1:] == "h" and s == "?m":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		s = float(v1) * float(t1)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "mph" and t[-1:] == "m" and s == "?m":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		t1 = float(t1) / 60
		s = float(v1) * float(t1)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
	
	if v[-3:] == "mph" and t[-1:] == "s" and s == "?m":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		s = float(s) * 1000
		print("Distance(s):",s,"m")
		
	if v[-3:] == "kph" and t[-1:] == "h" and s == "?mi":
		v1 = v[:-3]
		t1 = t[:-1]
		s = float(v1) * float(t1)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "kph" and t[-1:] == "m" and s == "?mi":
		v1 = v[:-3]
		t1 = t[:-1]
		t2 = float(t1) / 60
		s = float(v1) * float(t2)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "kph" and t[-1:] == "s" and s == "?mi":
		v1 = v[:-3]
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "mps" and t[-1:] == "s" and s == "?mi":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "mps" and t[-1:] == "h" and s == "?mi":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		s = float(v1) * float(t1)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "mps" and t[-1:] == "m" and s == "?mi":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		t1 = t[:-1]
		t1 = float(t1) / 60
		s = float(v1) * float(t1)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "mph" and t[-1:] == "h" and s == "?mi":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		s = float(v1) * float(t1)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "mph" and t[-1:] == "m" and s == "?mi":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		t1 = float(t1) / 60
		s = float(v1) * float(t1)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
	if v[-3:] == "mph" and t[-1:] == "s" and s == "?mi":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		t1 = t[:-1]
		t2 = float(t1) / 3600
		s = float(v1) * float(t2)
		s = float(s) / 1.60934
		print("Distance(s):",s,"mi")
	
#speed
	if v == "?kmph" and t[-1:] == "h" and s[-2:] == "km":
		t1 = t[:-1]
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "m" and s[-2:] == "km":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "s" and s[-2:] == "km":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "h" and s[-2:] == "m":
		t1 = t[:-1]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "m" and s[-2:] == "m":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "s" and s[-2:] == "m":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "h" and s[-2:] == "mi":
		t1 = t[:-1]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "m" and s[-2:] == "mi":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?kmph" and t[-1:] == "s" and s[-2:] == "mi":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		print("Speed(v):",v1,"kmph")
	
	if v == "?mph" and t[-1:] == "h" and s[-2:] == "km":
		t1 = t[:-1]
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "m" and s[-2:] == "km":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "s" and s[-2:] == "km":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "h" and s[-2:] == "m":
		t1 = t[:-1]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "m" and s[-2:] == "m":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "s" and s[-2:] == "m":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "h" and s[-2:] == "mi":
		t1 = t[:-1]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "m" and s[-2:] == "mi":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mph" and t[-1:] == "s" and s[-2:] == "mi":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 1.60934
		print("Speed(v):",v1,"mph")
	
	if v == "?mps" and t[-1:] == "h" and s[-2:] == "km":
		t1 = t[:-1]
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
	if v == "?mps" and t[-1:] == "m" and s[-2:] == "km":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
	if v == "?mps" and t[-1:] == "s" and s[-2:] == "km":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
	if v == "?mps" and t[-1:] == "h" and s[-2:] == "m":
		t1 = t[:-1]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
	if v == "?mps" and t[-1:] == "m" and s[-2:] == "m":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v,"mps")
	
	if v == "?mps" and t[-1:] == "s" and s[-2:] == "m":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		s1 = float(s1) / 1000
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
	if v == "?mps" and t[-1:] == "h" and s[-2:] == "mi":
		t1 = t[:-1]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
	if v == "?mps" and t[-1:] == "m" and s[-2:] == "mi":
		t1 = t[:-1]
		t1 = float(t1) / 60
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
	if v == "?mps" and t[-1:] == "s" and s[-2:] == "mi":
		t1 = t[:-1]
		t1 = float(t1) / 3600
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		v1 = float(s1) / float(t1)
		v1 = float(v1) / 3.6
		print("Speed(v):",v1,"mps")
	
#time
	if v[-3:] == "kph" and t == "?h" and s[-2:] == "km":
		v1 = v[:-3]
		s1 = s[:-2]
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "kph" and t == "?h" and s[-2:] == "m":
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "kph" and t == "?h" and s[-2:] == "mi":
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mph" and t == "?h" and s[-2:] == "km":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mph" and t == "?h" and s[-2:] == "m":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mph" and t == "?h" and s[-2:] == "mi":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?h" and s[-2:] == "km":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?h" and s[-2:] == "m":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?h" and s[-2:] == "mi":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?m" and s[-2:] == "km":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mps" and t == "?m" and s[-2:] == "m":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t,"m")
	
	if v[-3:] == "mps" and t == "?m" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mps" and t == "?s" and s[-2:] == "km":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "mps" and t == "?s" and s[-2:] == "m":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t,"s")
	
	if v[-3:] == "mps" and t == "?s" and s[-2:] == "mi":
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
		
	if v[-3:] == "kph" and t == "?m" and s[-2:] == "km":
		v1 = v[:-3]
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "kph" and t == "?m" and s[-2:] == "m":
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "kph" and t == "?m" and s[-2:] == "mi":
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mph" and t == "?m" and s[-2:] == "km":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mph" and t == "?m" and s[-2:] == "m":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mph" and t == "?m" and s[-2:] == "mi":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "kph" and t == "?s" and s[-2:] == "km":
		v1 = v[:-3]
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "kph" and t == "?s" and s[-2:] == "m":
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3060
		print("Time(t):",t1,"s")
	
	if v[-3:] == "kph" and t == "?s" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "mph" and t == "?s" and s[-2:] == "km":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "mph" and t == "?s" and s[-2:] == "m":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "mph" and t == "?s" and s[-2:] == "mi":
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
	print("="*45)
if choice == "std":
	print("""
Speed Distance Time
Speed KEY: kilometres per hour = kph
           meters per second = mps
           miles per hour = mph
		
Distance KEY: miles = mi
              metres = m
              kilometres = km
		
Time KEY: seconds = s
	  minutes = m 
	  hour = h 
	  seconds:minutes:hours = #
		
USE: 75kph 25mps 100mph 200mi 400m 3km 30s 45m 12h 
		
FOR UNKNOWN VALUE USE "?" (?km or ?h)
Type 'exit' to exit or 'back' to go back one
""")
	run = True
	while run == True:
		
		SpeedDistanceTime()
	




print("="*60)

resume = input("Go back to main menu? [y/n]: ")

if resume == "n":
	print("#"*60)	
	sys.exit()
elif resume == "y":
	os.execl(sys.executable, sys.executable, *sys.argv)
