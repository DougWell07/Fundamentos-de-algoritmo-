numero=int(input("Digite um número:"))
i=0

for i in range(0,11):
    if i <= 10:
        tab= i * numero
    print(f"{i} X {numero} = {tab}") 