lista= [1,2,3,5,6,7]
def soma_um(numero):
    return numero+1

lista_soma = list(map(soma_um, lista))
print(lista_soma)

## A mesma forma de fazer o modelo de cima, só que usando o for em lista ##

lista_soma2 = []
for x in lista:
    lista_soma2.append(soma_um(x))
print(lista_soma2)