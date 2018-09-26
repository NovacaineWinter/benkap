import numpy as np

s = '1,4,3'
b=16

def convertStringToList(string):

	#split input string into a python list (vector) of elements
	list_s_s = string.split(',')

	list_s =[]

	for i in range(0,len(list_s_s)):
		list_s.append(int(list_s_s[i]))

	return list_s

def convertListToString(inputList):

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



print kap(b,s)


