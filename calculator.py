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
''''''''''''''''''''''''''''''''''''''''  |miles -> kilometres        |    mile2km   |
                                          |kilometres -> miles        |    km2mile   |
                                          |feet -> metres             |    feet2m    |
					  |metres -> feet             |    m2feet    |
                                          |feet and inches -> metres  |  feetinch2m  |
                                          ''''''''''''''''''''''''''''''''''''''''''''
Choose a calculation or conversion by entering one of the commands
""")


choice = input("#>")

print("="*60)



def MeanModeMedian():
	
	
	nums = input("input all numbers with a space inbetween each of them: ")
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
				
				
		
	
if choice == "mmm":
	MeanModeMedian()

def fibonacci():
	series = [0, 1]
	length = int(input("how far into the fibonacci sequence do you want to go?: "))

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
		break
if choice == "fibo":
	fibonacci()

def den2bin():
	denary = int(input("please input a denary number: "))	
	binary = bin(denary)
	binary = str(binary)
	print("="*45)	
	print("Result: ",binary[2:])
if choice == "den2bin":	
	den2bin()
	

def bin2den():
	binary = int(input("please input a binary number: "), 2)
	print("="*45)	
	print("Result:",binary)
if choice == "bin2den":	
	bin2den()
	

def den2hex():
	denary = int(input("please input a denary number: "))
	hexadecimal = hex(denary)
	print("="*45)	
	print("Result:",hexadecimal[2:])
if choice == "den2hex":	
	den2hex()
	
def hex2den():
	hexinput = input("please input a hexadecimal number: ")
	hexadecimal = int(hexinput, 16)
	print("="*45)	
	print("Result:",hexadecimal)
if choice == "hex2den":	
	hex2den()
	
def bin2hex():
	binary = int(input("please input a binary number: "), 2)
	hexadecimal = hex(binary)
	print("="*45)
	print("Result:",hexadecimal[2:])
if choice == "bin2hex":
	bin2hex()
	
def hex2bin():
	hexinput = input("please input a hexidecimal number: ")
	hexadecimal = int(hexinput, 16)
	binary = bin(hexadecimal)
	print("="*45)	
	print("Result:",binary[2:])
if choice == "hex2bin":	
	hex2bin()

def calculator():
	print("REMEMBER * = times and / = divide")	
	print("your format should look like this: 1 + 1")	
	Input = input("input your calcution: ")
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
if choice == "calc":
	calculator()

def cm2inch():
	inp = float(input("input the amount of centimetres: "))
	result = inp / 2.54
	print("="*45)	
	print(result,"inches")
if choice == "cm2inch":
	cm2inch()

def inch2cm():
	inp = float(input("input the amount of inches: "))
	result = inp * 2.54
	print(45*"=")	
	print(result,"cm")
if choice == "inch2cm":
	inch2cm()

def mile2km():
	inp = float(input("input the amount of miles: "))
	result = inp * 1.609
	print(45*"=")	
	print(result,"km")
if choice == "mile2km":
	mile2km()

def km2mile():
	inp = float(input("input the amount of kilometres: "))
	result = inp / 1.609
	print(45*"=")	
	print(result,"miles")
if choice == "km2mile":
	km2mile()

def power():
	print("the format shoud look like this 2 8")	
	inp = input("please input here: ")
	tmp = inp.split()
	tmp1 = (tmp[0])
	tmp2 = (tmp[1])
	result = float(tmp1)**float(tmp2)
	print(45*"=")	
	print(result)
if choice == "power":
	power()

def feet2m():
	inp = float(input("please input amount of feet: "))
	result = inp / 3.281
	print("="*45)
	print(result,"m")
if choice == "feet2m":
	feet2m()

def m2feet():
	inp = float(input("please input amount of metres: "))
	result = inp * 3.281
	print("="*45)
	print(result,"feet")
if choice == "m2feet":
	m2feet()


def feetinch2m():
	print("the format is: feet inch")
	inp = input("input feet and inches: ")
	tmp = inp.split()
	feet = float(tmp[0])
	inch = float(tmp[1])
	fmetres = feet / 3.281
	imetres = inch * 2.54
	imetres = imetres / 100
	metres = imetres + fmetres
	print("="*45)
	print(metres,"m")
if choice == "feetinch2m":
	feetinch2m()

def root():
	inp = float(input("input a number: "))
	result = math.sqrt(inp)
	print(result)
if choice == "root":
	root()
	


def quadratic():
	a = input("a: ")
	b = input("b: ")
	c = input("c: ")


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
if choice == "quad":
	quadratic()

def pythagoras():
	print("a^2 x b^2 = c^2")
	print("for unkown value enter \"?\"")
	a = input("Value of a: ")
	b = input("Value of b: ")
	c = input("Value of c: ")
	
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
if choice =="pyth":
	pythagoras()
	
def SpeedDistanceTime():	
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
""")
		
	s = input("Distance(s): ")
	v = input("Speed(v): ")
	t = input("Time(t): ")
	
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
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "kph" and t == "?h" and s[-2:] == "m":
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "kph" and t == "?h" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mph" and t == "?h" and s[-2:] == "km":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mph" and t == "?h" and s[-2:] == "m":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mph" and t == "?h" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?h" and s[-2:] == "km":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?h" and s[-2:] == "m":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?h" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t = float(s1) / float(v1)
		print("Time(t):",t,"h")
	
	if v[-3:] == "mps" and t == "?m" and s[-2:] == "km":
		print("test")
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
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t,"s")
	
	if v[-3:] == "mps" and t == "?s" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 3.6
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
		
	if v[-3:] == "kph" and t == "?m" and s[-2:] == "km":
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "kph" and t == "?m" and s[-2:] == "m":
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "kph" and t == "?m" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mph" and t == "?m" and s[-2:] == "km":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mph" and t == "?m" and s[-2:] == "m":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "mph" and t == "?m" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 60
		print("Time(t):",t1,"m")
	
	if v[-3:] == "kph" and t == "?s" and s[-2:] == "km":
		print("test")
		v1 = v[:-3]
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = float(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "kph" and t == "?s" and s[-2:] == "m":
		print("test")
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
		t1 = foat(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "mph" and t == "?s" and s[-2:] == "km":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		t1 = float(s1) / float(v1)
		t1 = foat(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "mph" and t == "?s" and s[-2:] == "m":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) / 1000
		t1 = float(s1) / float(v1)
		t1 = foat(t1) * 3600
		print("Time(t):",t1,"s")
	
	if v[-3:] == "mph" and t == "?s" and s[-2:] == "mi":
		print("test")
		v1 = v[:-3]
		v1 = float(v1) * 1.60934
		s1 = s[:-2]
		s1 = float(s1) * 1.60934
		t1 = float(s1) / float(v1)
		t1 = foat(t1) * 3600
		print("Time(t):",t1,"s")
if choice == "std":
		SpeedDistanceTime()
	




print("="*60)

resume = input("Go back to main menu? [y/n]: ")

if resume == "n":
	print("#"*60)	
	sys.exit()
elif resume == "y":
	os.execl(sys.executable, sys.executable, *sys.argv)

