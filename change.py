def change():
    expense = 23.75
    money = 100
print (f"Ingresar gasto:")
expense = 23.75
print (expense)
print (f"Dinero recibido:")
money = 100
print (money)
print (f"Vuelto:")
change = (money-expense)
print (change)
print (f"Pesos:")
print (int (change))
centavos = (change-int(change))*(int(money))
print (f"Centavos:")
print (int(centavos))
