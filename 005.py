# coding: utf-8

import math

i=1
k=1
flag=-1
while (flag==-1):
	flag=0	
	for i in range(11,21):
		if (k%i!=0):
			flag=-1		
	k+=1
print "Resposta: ",k-1

