#Verificador de múltiplos de 3, de 1 a 500

soma = 0
contador = 0
for c in range (1,501,2):
    if c % 3 == 0:
       soma += c
       contador += 1
        
print('a soma de todos os valores é {}'.format(soma)    )
print( 'a quantidade de elementos somadas é {}'.format(contador))