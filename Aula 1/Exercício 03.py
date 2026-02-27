dia= float(input("Diigte a quantidade de dias:"))
horas= float(input("Diigte a quantidade de horas:"))
minutos= float(input("Diigte a quantidade de minutos:"))
segundos= float(input("Diigte a quantidade de segundos:"))
seg_dia= 86400*dia
seg_hora=3600*horas
seg_minutos=60*minutos
seg_segundos=segundos
total_seg= seg_dia + seg_hora + seg_minutos + seg_segundos
print("O valor total em segundos é de: %.2f" %total_seg)