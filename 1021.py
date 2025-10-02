valor = float(input())
resto = int(round(valor * 100))
print("NOTAS:")
for nota in [100, 50, 20, 10, 5, 2]:
    qtd = resto // (nota * 100)
    resto %= (nota * 100)
    print(f"{qtd} nota(s) de R$ {nota}.00")
print("MOEDAS:")
qtd = resto // 100
resto %= 100
print(f"{qtd} moeda(s) de R$ 1.00")
for moeda in [50, 25, 10, 5, 1]:
    qtd = resto // moeda
    resto %= moeda
    print(f"{qtd} moeda(s) de R$ 0.{moeda:02d}")