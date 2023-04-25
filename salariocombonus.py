vendedor = str(input())
S = float(input())
V = float(input())

bonus = float(V * (15/100))
total = S + bonus

print(vendedor)
print("R$ %0.2f" %total)