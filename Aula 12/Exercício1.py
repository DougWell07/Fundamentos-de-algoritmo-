arquivo= open("pares.txt", "w")

for pares in range(0,1001,2):
    arquivo.write(f"Numeros:{pares}\n")
arquivo.close()

arquivo= open("impares.txt", "w")

for impares in range(1,1000,2):
    arquivo.write(f"Numeros:{impares}\n")
arquivo.close()