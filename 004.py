# coding: utf-8

import math

maior=0
for i in range(1,1000):
	for j in range (1,1000):
		num= i*j
		numstring = str(num)
		palindromo = True
		for k in range (0,len(numstring)):
			if (numstring[k]!=numstring[len(numstring)-1-k]):
				palindromo = False
		if (palindromo):
			if (num>maior):
				maior=num		
		
print "Valor total: ",maior

