# coding: utf-8

import math

produto=0
a=1
while (produto==0):
	for i in range (0,a):
		b=i
		c=(math.sqrt(a**2+b**2))
		if (math.floor(c)==c):
			if (a+b+c==1000):
				produto=a*b*c
	a+=1

print "Resposta: ",produto

