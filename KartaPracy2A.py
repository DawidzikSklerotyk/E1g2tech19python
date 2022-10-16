import math
# zad 1
a = int(input("Liczba A: "))
b = int(input("Liczba B  "))
if (a + b) % 2 == 0:
 print("TAK")
else:
  print("NIE")
# zad 2
a = int(input("Liczba A:  "))
b = int(input("Liczba B:  "))
if (a + b) / 2 > math.sqrt(a * b):
  print("średnia arytmetyczna jest większa")
else:
  print("średnia arytmetyczna jest mniejsza")
# zad 3
a = int(input("Liczba A:  "))
b = int(input("Liczba B:  "))
c = int(input("Liczba C:  "))
if a == b or a == c:
  print("TAK: " + repr(a))
elif b == c:
  print("TAK: " + repr(b))
else:
  print("NIE")
# zad 4
a = int(input("Liczba A:  "))
b = int(input("Liczba B:  "))
c = int(input("Liczba C:  "))
d = int(input("Liczba D:  "))
if a < b and c and d:
  print(a)
elif b < a and c and d:
  print(b)
elif c < a and b and d:
  print(c)
elif d < a and b and c:
  print(d)
# zad 5
a = int(input("Liczba A:  "))
b = int(input("Liczba B:  "))
c = int(input("Liczba C:  "))
if a < c + b or b < a + c or c < a + b:
  print("TAK")
else:
  print("NIE")
# zad 6
print("Podaj kąty trójkątów")
a = int(input("Liczba A:  "))
b = int(input("Liczba B:  "))
c = int(input("Liczba C   "))
if a < 90 and b < 90 and c < 90:
  print("ostrokątny")
elif a == 90 or b == 90 or c == 90:
  print("prostokątny")
elif a > 90 or b > 90 or c > 90:
  print("rozwartokątny")