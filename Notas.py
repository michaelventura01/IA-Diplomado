print('Ingrese Nombre de Persona:')
nombre = input()

print('ingrese nota 1')
n1 = int(input())

print('ingrese nota 2')
n2 = int(input())

print('ingrese nota 3')
n3 = int(input())

print('ingrese nota 4')
n4 = int(input())

prom = int((n1+n2+n3+n4)/4)
if(prom>70):
    print('Promedio Generado: '+str(prom) +' Aprobado '+nombre)
else:
    print('Promedio Generado: ' + str(prom) + ' Reprobado '+nombre)




