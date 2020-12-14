# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:04:19 2020

@author: Tirth
"""



def fact(n):
	total = 1
	for i in range(1,n+1):
		total = total*i

	return total

n = int(input('Enter a number: '))
total = fact(n)
print(total)




    
        
    
    
    
    