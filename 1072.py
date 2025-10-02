quant = int(input())
dentro = 0
fora = 0
for i in range(quant):
   numero = int(input())
   if 10 <= numero <= 20:
      dentro += 1
   else:
      fora +=1
print(f"{dentro} in")
print(f"{fora} out")