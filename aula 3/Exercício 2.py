numero1=int(input("Digite um número:"))
numero2=int(input("Digite outro número:"))
numero3=int(input("Digite outro número:"))

if numero1 > numero2 and numero2> numero3:
   print("O a sequecia é de:", numero1, numero2, numero3)
if numero1 > numero3 and numero3 > numero1:
    print("O a sequecia é de:", numero1, numero3, numero2)
if numero2 > numero1 and numero1 > numero3:
    print("O a sequecia é de:", numero2, numero1, numero3)
if numero2 > numero3 and numero3 > numero1:
    print("O a sequecia é de:", numero2, numero3, numero1)
if numero3 > numero2 and numero2 > numero1:
    print("O a sequecia é de:", numero3, numero2, numero1)
if numero3 > numero1 and numero1 > numero2:
    print("O a sequecia é de:", numero3, numero1, numero2)
    

    

    
