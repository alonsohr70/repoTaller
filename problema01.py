print("Introduce tu edad: ")
edad = int(input())
if edad >=0 and edad<4 :
    print("Entrada GRATIS")
elif edad >= 4 and edad <= 12 :
    print("Boleto Infantil: Monto a pagar $40.00")
elif edad >= 13 and edad <= 59 :
    print("Boleto Adulto: Monto a pagar $70.00")
elif edad >= 60 :
    print("Boleto Adulto Mayor: Monto a pagar: $",70-35)
else :
    print("Edad no válida")

