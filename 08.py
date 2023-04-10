inicio = int(input())
fim = int(input())
horas = (fim - inicio)//60
minutos = (fim - inicio)%60
print(horas, ":" , minutos)