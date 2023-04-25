numero = int(input())

print(str (numero)) 

cem = int(numero / 100)
numero = numero % 100

cinquenta = int(numero / 50)
numero = numero % 50

vinte = int(numero / 20)
numero = numero % 20

dez = int (numero / 10)
numero = numero % 10

cinco = int(numero / 5)
numero = numero % 5

dois = int(numero / 2)
numero = numero % 2

um = numero

print(str (cem), "nota(s) de R$ 100,00")
print(str (cinquenta), "nota(s) de R$ 50,00")
print(str (vinte), "nota(s) de R$ 20,00")
print(str (dez), "nota(s) de R$ 10,00")
print(str (cinco), "nota(s) de R$ 5,00")
print(str (dois), "nota(s) de R$ 2,00")
print(str (um), "nota(s) de R$ 1,00" )