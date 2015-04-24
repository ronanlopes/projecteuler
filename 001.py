# coding: utf-8

multiplos3=0
multiplos5=0

for i in range(3,1000):
	if (i%3==0):
		multiplos3+=i
	elif (i%5==0):
		multiplos5+=i
multiplostotal=multiplos3+multiplos5
print "Valor total:",multiplostotal
