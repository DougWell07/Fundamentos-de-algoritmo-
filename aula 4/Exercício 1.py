for i in range(1,11):
   num=int(input("Digite um número:"))
   if num > 0:
         e_primo:True 
         for d in range(2, int(num**0.5)+1):
              if (num % i == 0):
                   primo=0
                   break

total += primo
print(f"Você digitou {total} números primos de um total de 10 números")