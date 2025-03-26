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
   # Si no se pasa ningún argumento, solicitamos un número
   num = int(input("Debe informar un número: "))
elif "-" in sys.argv[1]:  # Si el argumento es un rango
   arg = sys.argv[1].split('-')
   if len(arg) == 2:  # Rango con ambos límites
       if arg[0] == '':  # Si el límite inferior está vacío, lo ponemos en 1
           start = 1
       else:
           start = int(arg[0])

       if arg[1] == '':  # Si el límite superior está vacío, lo ponemos en 60
           end = 60
       else:
           end = int(arg[1])

       for i in range(start, end + 1):
           print(f"Factorial de {i} es {factorial(i)}")
   sys.exit()
else:
   num = int(sys.argv[1])

print("Factorial ", num, "! es ", factorial(num))
