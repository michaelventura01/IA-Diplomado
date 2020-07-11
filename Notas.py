print('Ingrese Nombre de Persona:')
nombre = input()

cantidad = 4
aprobado = 70

notas = []
for cuenta in range(0, cantidad):
    print('ingrese nota '+str(cuenta+1))
    nota = int(input())
    notas.append(nota)

prom = 0
for score in range(0, cantidad):
    prom += notas[score]


if((prom/4)>aprobado):
    print('Promedio Generado: '+str(prom/4) +' Aprobado '+nombre)
else:
    print('Promedio Generado: ' + str(prom/4) + ' Reprobado '+nombre)




