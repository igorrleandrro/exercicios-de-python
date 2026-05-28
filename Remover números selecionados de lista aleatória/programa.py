import random
qtd = int(input('quantos numeros? '))
lista= []

for i in range(qtd):
    n = random.randint(1, 10)
    lista.append (n)

print (lista)

x = int(input('numero: '))

n=0
lista2 = []
achou = False
while n < len(lista):
    if lista[n] == x:
        del lista[n]
    else: n +=1
        
print (lista)