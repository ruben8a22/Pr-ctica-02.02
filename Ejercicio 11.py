#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a
# intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un
# programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

cantidadInicial = float(input("Introduce una cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 1.04
ahorrosAño1 = cantidadInicial * interes
print("Ahorros despues del primer año: " + str(round(ahorrosAño1, 2)))
ahorrosAño2 = ahorrosAño1 * interes
print("Ahorros despues del segundo año: " + str(round(ahorrosAño2, 2)))
ahorrosAño3 = ahorrosAño2 * interes
print("Ahorros despues del tercer año: " + str(round(ahorrosAño3, 2)))