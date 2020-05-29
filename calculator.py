#!/bin/python3
#Denary, Binary, Hexadecimal number calculator
import sys
import os
import math


print("ULTIMATE CALCULATOR!")
print("="*45)
print("OPTIONS..........................COMMANDS")
print("~"*45)
print("normal calculator....................calc")
print("square root..........................root")
print("power of............................power")
print("quadratic............................quad")
print("denary -> binary..................den2bin")
print("binary -> denary..................bin2den")
print("denary -> hexadecimal.............den2hex")
print("hexadecimal -> denary.............hex2den")
print("binary -> hexadecimal.............bin2hex")
print("hexadecimal -> binary.............hex2bin")
print("centimetres -> inches.............cm2inch")
print("inches -> centimetres.............inch2cm")
print("miles -> kilometres...............mile2km")
print("kilometres -> miles...............km2mile")
print("feet -> metres.....................feet2m")
print("metres -> feet.....................m2feet")
print("feet and inches -> metres......feetinch2m")


print("="*45)

choice = input("which command do you want to use?: ")

print("="*45)

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
	Input = input("input your calcutions REMEMBER * = times and / = divide: ")
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
	a = float(input("a: "))
	b = float(input("b: "))
	c = float(input("c: "))

	b1 = -float(b)


	bsqr = b ** 2
	sqrt = bsqr - 4 * a * c
	sqrt1 = sqrt ** 0.5


	x1 = -b + sqrt1
	x2 = 2 * a

	x3 = -b - sqrt1
	x4 = 2 * a

	x_p = float(x1) / float(x2)
	x_n = float(x3) / float(x4)


	print("X = ",x_p)
	print("-X = ",x_n)
if choice == "quad":
	quadratic()




print("="*45)

resume = input("do you want to restart? [y/n]: ")

if resume == "n":
	print("#"*45)	
	sys.exit()
elif resume == "y":
	os.execl(sys.executable, sys.executable, *sys.argv)


