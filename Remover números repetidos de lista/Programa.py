qtd=int(input('digite o tamanho da lista: '))
lista=[]

for _ in range(qtd):
    n = int(input('digite um número pra lista: '))
    lista.append (n)
print (lista)

m = 0
achou = False

while m < len(lista):
    j = m+1
    while j < len(lista):
        if lista[m] == lista[j]:
            del lista [j]
            achou = True
        else:
            j+=1
    m+=1

if achou == True:
    print (lista)
else:
    print (f'não tem repetições')