maiornum = -1
posicaomaiornum = 0
for i in range(100):
   valor = int(input())
   if valor > maiornum:
      maiornum = valor
      posicaomaiornum = i + 1
print(maiornum)
print(posicaomaiornum)