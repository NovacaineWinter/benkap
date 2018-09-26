import numpy as np

s = '4,5,9'
b=10

#b is base, s is string of input numbers comma separated, with k elements
def kap(b,s):

	#split input string into a python list (vector) of elements
	list_s_s = s.split(',')

	list_s =[]

	for i in range(0,len(list_s_s)):
		list_s.append(int(list_s_s[i]))
	
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

	print(np.dot(mat_s_asc,bk_mat))
	

kap(b,s)