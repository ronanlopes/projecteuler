# coding: utf-8

def fibonacci (n):
	if (n==1):
		return 1	
	elif (n==2):
		return 2
	else:
		return fibonacci(n-2) + fibonacci(n-1)

i=1
soma=0
fib=fibonacci(1);
while fib<4000000:
	if (fib%2==0):
		soma+=fib
	i+=1
	fib=fibonacci(i)
print "Valor total: ",soma
