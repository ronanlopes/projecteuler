# coding: utf-8

import math

i=1
k=3
qtdprimo=1
while (qtdprimo!=10001):
	flag=0
	for i in range (2,int(math.sqrt(k)+2)):
		if (k%i==0):
			flag=-1
	if (flag==0):
		qtdprimo+=1
	k+=1
print "Resposta: ",k-1

