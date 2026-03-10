i=0
while True:
  n=int(input("Informe um número:"))
  if n > 10:
    print("Valor inválido")
    n += 1 
    break
  else:
    if n == 0 or 10:
      print("Número aceito")
    break
        
