# coding: utf-8

import math

def is_prime(n):
	if (n==2):
		return True
	for i in range (2, int(math.sqrt(n)+2)):
		if (n%i==0):
			return False
	return True

soma=0
for i in range(2,2000001):
	if (is_prime(i)):
		soma+=i

print "Resposta: ",soma

