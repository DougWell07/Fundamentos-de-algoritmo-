arquivo= open("pares.txt", "a")

for pares in range(0,1001,4):
    arquivo.append(f"Numero multiplos de 4:{pares}\n")
arquivo.close()

