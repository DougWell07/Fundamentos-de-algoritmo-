import math
altura=float(input("Digite a altura do produto:"))
raio=float(input("Digite o raio do cilíndro:"))
area_base= 3.1415 * (raio ** 2)
area_lateral= altura + (2 * 3.1415 * raio)
area_cilindro= area_base + area_lateral
litros= area_cilindro/3
latas= litros/5

if latas == 1:
    valor_unit = 50.00
if latas == 2:
    valor_unit = 48.00
if latas == 3:
     valor_unit = 46.00
else:
     valor_unit = 45.00
    

custo_total= latas * valor_unit  
print(" Área total: {area_cilindro:2.f}m2")
print( "latas necessárias: {latas}")
print("Área total: {custo_total}m2")
      

