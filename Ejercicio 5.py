#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe
# mostrar por pantalla la paga que le corresponde.

horasTrabajadas = int(input("Cuantas horas trabajas?"))
costeLaHora = int(input("Cual es el coste por hora?"))

print("Tu paga es")
print(horasTrabajadas * costeLaHora)