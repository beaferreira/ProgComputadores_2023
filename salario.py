funcionario = str(input())
horas = int(input())
valor = float(input())

pagamento = horas * valor

print(funcionario)
print("R$ " "{:.2f}".format(pagamento))
