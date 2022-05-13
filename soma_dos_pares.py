#Soma de números pares
contador = 0
soma = 0

for c in range (1,7):
   valor = int(input('digite o {}º valor '.format(c)))
   if valor % 2 == 0:
       soma += valor
       contador += 1        

print ('você informou {} números pares, e a soma foi {}'.format(contador, soma))
