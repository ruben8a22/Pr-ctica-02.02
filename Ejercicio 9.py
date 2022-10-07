#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre
# por pantalla el capital obtenido en la inversión.

inversion = float(input("Cuanto dinero quiere invertir?"))
interesAnual = float(input("Cuanto %?"))
años = int(input("Cuantos años?"))

capitalObtenido = inversion * (interesAnual / 100) * años + (inversion)

print ("El capital obtenido en la inversion es de " + str(inversion) + " es " + str(capitalObtenido))

