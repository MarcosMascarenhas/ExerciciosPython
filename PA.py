#Progressão Aritimética 

print ('='*30)
print ('OS 10 TERMOS DE UMA PA')
print ('='*30)

termo1 = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão'))
décimo = termo1 + (10-1) * razao

for c in range (termo1, décimo + razao , razao):
    print (c, end = ' → ')

print ('ACABOU!')

