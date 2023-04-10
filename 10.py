item = int(input())
quant = int(input())
pagar = int(input())

pagamento =  item * quant
troco = pagar - pagamento

print("A pagar:", pagamento, "Troco:", troco)