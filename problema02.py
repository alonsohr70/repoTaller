#ciclos
calificacion = 0
sumacalificacion = 0
totalcalificaciones = 0
calificacion = int(input("Introduce una calificación: "))
while calificacion >= 0 :
    sumacalificacion = sumacalificacion + calificacion
    totalcalificaciones = totalcalificaciones + 1
    calificacion = int(input("Introduce una calificación: "))

if totalcalificaciones == 0 :
    promedio=0
    totalcalificaciones = 0
else:
    promedio = sumacalificacion / totalcalificaciones

print("Calificaciones leidas:",totalcalificaciones)
print("Promedio de calificaciones: ",promedio)

