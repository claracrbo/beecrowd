testes = int(input())
total = 0
coelhos = 0
sapos = 0
ratos = 0
for i in range(testes):
  numero, tipo = input().split()
  numero = int(numero)
  total += numero
  if tipo == "C":
      coelhos += numero
  if tipo == "R":
      ratos += numero
  if tipo == "S":
      sapos += numero
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos*100.0/total:.2f} %")
print(f"Percentual de ratos: {ratos*100.0/total:.2f} %")
print(f"Percentual de sapos: {sapos*100.0/total:.2f} %")