import numpy as np


def convertStringToList(inputString):
	#split string into a list by the comma, then convert each into an int	
	return map(int,(inputString.split(',')))

def convertListToString(inputList):
	#dead easy - take list
	return ','.join(map(str, inputList))

def value(b,s):
	#b is base, s is string of input numbers comma separated, with k elements
	list_s = convertStringToList(s)
	
	#work out k - the nubmer of elements in s
	k = len(list_s)

	#convert s to numpy matrix
	mat_s = np.array(list_s)

	#sort into ascending order
	mat_s_asc = np.sort(mat_s)

	bk = []

	for i in range(1,(k+1)):		
		bk.append(b**(i-1) - b**(k-i))

	bk_mat = np.array(bk)

	v = (np.dot(mat_s_asc,bk_mat))
	
	return v

def valueToBase(v,b):
	maxPower = int(np.floor(np.log(v)/np.log(b)))

	output = []

	for i in reversed(range(0,(maxPower+1))):
		power = b**i
		number = int(np.floor(v/(power)))
		output.append(number)
		v=(v-(power*number))

	return output

def kap(b,s):
	#this function must deal with putting the nececary leading zero on to the output of valueToBase()
	k = len(convertStringToList(s))

	output = valueToBase(value(b,s),b)

	if len(output) != k:
		output.insert(0,0)

	return convertListToString(output)

def decompose(b,s):
	l = convertStringToList(s)
	output =[]
	for x in range(0,b):
		num = 0
		for z in range(0,len(l)):	
			if l[z] == x:
				num = num +1
				
		output.append(num)

	return output

def recompose(b,inp):
	nums = range(0,b)
	output = []
	for i in nums:
		for j in range(0,inp[i]):
			output.append(i)

	return output

#print recompose(b,decompose(b,s))

def addLeadingZeros(numAsStr,k):
	#this currently doesnt deal with commas - dont know if that is a problem yet
	length = len(numAsStr)
	print numAsStr
	if(length < k):
		for i in range(0,k-length):
			numAsStr='0'+numAsStr


def addCommas(str):
	pass

#function of b and k that outputs all acceptable s

def inputs(b,k):
#having trouble with this function - considering making something that works like a rolling counter

	numbers = []
	number = ''
	for i in range(0,k):
		pass
	numbers = map(str,numbers)
	numbers = [addLeadingZeros(n, k) for n in numbers]
	return numbers
	
