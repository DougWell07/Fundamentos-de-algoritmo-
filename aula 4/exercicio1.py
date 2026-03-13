total_primos=0
n=int(input("Digite a quantidade de núemmros:"))
for i in range(0,n):
    x=int(input("Digite um número:"))
    if x > 1:
        primo = 1
        for j in range(2,x):
            if x % j == 0:
                primo=0
                break 
        total_primos += primo
print(f"Os números primos são {total_primos}") 


