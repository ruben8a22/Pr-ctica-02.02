#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente
# <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el
# resto de la división entera respectivamente.

numeroEntero1 = int(input("Escriba un numero entero"))
numeroEntero2 = int(input("Escriba otro numero entero"))
cociente = int(numeroEntero1 / numeroEntero2)
print(numeroEntero1, " dividido entre", numeroEntero2, " da un cociente de", cociente)

resto =(str(int(numeroEntero1) % int(numeroEntero2)))
print("El resto es", resto)