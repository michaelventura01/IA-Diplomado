n = int(input("Verificar numero: "))
multiplo=0

for count in range(2,n):
    if (n % count == 0):
        multiplo += 1

if(multiplo==0):
    print("es primo")
else:
    print("Es Compuesto")
