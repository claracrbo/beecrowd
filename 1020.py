N = int(input())
anos = N // 365
resto = N % 365
meses = resto // 30
dias = resto % 30
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")