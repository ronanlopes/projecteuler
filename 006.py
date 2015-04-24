# coding: utf-8

import math

quadradosoma=0
somaquadrado=0
for i in range(1,101):
	somaquadrado+=i**2
	quadradosoma+=i
quadradosoma=quadradosoma**2
		
print "Resposta: ",quadradosoma-somaquadrado

