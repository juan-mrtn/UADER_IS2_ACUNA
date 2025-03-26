#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:
   num = int(input("Debe informar un número: "))
elif "-" in sys.argv[1]:  # Si el argumento es un rango
   start, end = map(int, sys.argv[1].split('-'))
   for i in range(start, end + 1):
       print(f"Factorial de {i} es {factorial(i)}")
   sys.exit()
else:
   num = int(sys.argv[1])

num=int(sys.argv[1])
print("Factorial ",num,"! es ", factorial(num)) 

