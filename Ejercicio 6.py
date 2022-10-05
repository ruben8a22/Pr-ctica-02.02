#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de
# todos los enteros desde 1 hasta . La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:

numeroEntero = int(input("Introduce un numero entero"))
suma = int(((numeroEntero * (numeroEntero + 1)) / 2))
print("La suma de los primeros números enteros desde 1 hasta", numeroEntero, "es:", suma)