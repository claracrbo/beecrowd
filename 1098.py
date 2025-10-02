i = 0
while i<= 2:
   j = 1
   for a in range(3):
      if i != int(i):
         print(f"I={i:.1f} J={j+i:.1f}")
      else:
         print(f"I={i:.0f} J={j+i:.0f}")
      j += 1
   i += 0.2