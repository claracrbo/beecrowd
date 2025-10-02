N = int(input())
print(N)
for cedula in [100, 50, 20, 10, 5, 2, 1]:
    qtd = N // cedula
    N %= cedula
    print(f"{qtd} nota(s) de R$ {cedula},00")