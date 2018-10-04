import numpy as np
import sys	#Gives access to the command line arguments :O Le what? it sets a default language?

#
def expo(x):
	return np.exp(x)	#return the np e^x function
	
#
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))
		
def main():
	n = 10
	
	#
	if(len(sys.argv)>1):		#len tells you the length of the array :o
		n = int(sys.argv[1])	#sys.argv is the variable arguments in the system?
								#this lets us grap the argument inputted in the command line, and put it in the array as an integer
	show_expo(n)
	
	
	
	#
if __name__ == "__main__":
	main()
	