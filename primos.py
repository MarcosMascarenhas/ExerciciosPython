from time import sleep
n = int (input('Digite um numero '))
divs = 0
print('Analisando...')
sleep(1.5)
for c in range (1, n +1 ):
    if n % c == 0:
        divs += 1
        print ('\033[33m', end= ' ')
    else:
        print('\033[31m', end= ' ')
    print (c)
    
print ('o número {} foi divisível {} vezes'.format(n,divs))
if divs == 2:
    print('Por isso {} é um número PRIMO'.format (n))
else:
    print('Por isso {} NÃO é um número primo.'.format (n))
