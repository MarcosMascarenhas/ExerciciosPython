#Contador de maioridades e menoridades.

from datetime import date

atual = date.today().year
contador_menor = 0
contador_maior = 0

for pessoa in range (1,8):
    nascimento = int(input('Em que ano nasceu a {}° pessoa?'.format(pessoa)))
    idade = atual - nascimento

    if idade >= 21:
        contador_maior += 1
    else:
        contador_menor += 1

print ('Temos {} pessoas de maior e {} pessoas de menor idade'.format(contador_maior, contador_menor))