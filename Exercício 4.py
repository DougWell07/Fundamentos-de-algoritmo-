i = 0 
maior = 0

while i < 6:
    valor = int(input())
    if valor > maior:
        maior = valor 
    i += 1

print(f"O maior valor = {maior}")

