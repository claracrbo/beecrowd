soma = 0
quant = 0
for i in range(6):
    valor = float(input())
    if valor>0:
     soma = soma + valor
     quant = quant + 1
print(f"{quant} valores positivos")
print(f"{soma / quant:0.1f}")