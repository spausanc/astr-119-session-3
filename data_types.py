import numpy as np

#integers

i = 10
print(type(i))

a_i = np.zeros(i,dtype=int)	#declare an array of ints. Otherwise will be floats
print(type(a_i))			#will return ndarray?
print(type(a_i[0]))			#will return integers of 64 bits?

#floats

x = 119.0 					#floating point number
print(type(x))				#print out the data type of x

y = 1.19e2					#floating point number
print(type(y))				#print out the data type of y

z = np.zeros(i,dtype=float)	#declare array of floats
print(type(z))				#will return nd array
print(type(z[0]))			#will return float64
