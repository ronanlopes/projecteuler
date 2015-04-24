# coding: utf-8

import math

maior=0
for i in range(3,int(math.sqrt(600851475143))+2):
	flag=0
	for j in range (2,int(math.sqrt(i))+2):
		if (i%j==0):
			flag=-1
	if (flag==0 and 600851475143%i==0):
		if (i>maior):
			maior=i
		
print "Valor total: ",maior

