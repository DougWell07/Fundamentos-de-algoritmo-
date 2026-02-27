preco= float(input("Digite o preço do produto:"))
codigo= int(input("Digite o código de origem do produto:"))

procedencia = "importado"

if codigo== 1:
  procedencia= "Sul"
if codigo== 2:
  procedencia= "Norte" 
if codigo== 3:
    procedencia= "Leste"
if codigo== 4:
    procedencia= "Oeste"
if codigo== 5  or codigo== 6:
    procedencia= "Nordeste" 
if codigo== 7 or codigo== 8 or codigo== 9:
    procedencia= "Suldeste"
if codigo == 10 <= 20:
    procendencia= "Centro-oeste"
if codigo== 25 <= 30:
    procendencia= "Noroeste"
if codigo > 30:
    procendencia= "Importado"
    
print(f"Preço R${preco:.3f}")
print("Procedencia", procedencia)
