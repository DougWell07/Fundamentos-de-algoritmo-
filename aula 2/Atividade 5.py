ano = int(input("Digite o ano que você nasceu:"))
ano_atual = int(input("Digite o ano que estamos:"))
idade = ano_atual - ano
if idade >= 18:
 print("Você ja pode tirar CNH")
else:
    print("Você ainda não pode tirar a CNH")