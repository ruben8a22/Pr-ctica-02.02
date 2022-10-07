#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un
# programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el
# precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

precioPanDelDia = 3.49
descuento = 60

barrasNoDia = int(input("Cuantas barras han vendido que no son del dia?"))
barrasDelDia = int(input("Cuantas barras del dia has vendido?"))
print("La barra de pan cuesta", precioPanDelDia)
descuentoPanAntiguo = (precioPanDelDia * 0.6) + barrasDelDia
print(descuentoPanAntiguo)