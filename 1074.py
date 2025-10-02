N = int(input())
for i in range(N):
   val = int(input())
   if val == 0:
      print("NULL")
   else:
      string1 = "EVEN" if val % 2 == 0 else "ODD"
      string2 = "POSITIVE" if val > 0 else "NEGATIVE"
      print(f"{string1} {string2}")