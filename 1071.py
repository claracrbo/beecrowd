def main():
   x = int(input())
   y = int(input())
   cont = x - 1
   soma = 0
   while cont > y:
      if cont % 2 != 0:
         soma = soma + cont
      cont =  cont - 1
   print(soma)
main()