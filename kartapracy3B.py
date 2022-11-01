# zad 1
for i in range(1, 31):
  print(i, end=" ")
# zad 2
for i in range(1, 100, 2):
  print(i**2, end=" ")
# zad 3
for i in range(1000, 10001):
  if i % 379 == 0:
    print(i)
# zad 4
for i in range(100, 1000):
  if i % 11 == 0:
    print(i)
# zad 5
suma = 0
ile = int(input("ile liczb: "))
for i in range(0, ile):
  n = int(input("podaj liczbę: "))
  suma = suma + n
  if i == ile - 1:
   print(suma)
# zad 6
n = int(input("ile liczb poczatkowych: "))
suma = 0
for i in range(0, n*2, 2):
  suma = suma + i
  if i == n*2 - 2:
   print(suma)
# zad 7
n = int(input("Ile liczb poczatkowych: "))
suma = 0
for i in range(11, 10 + ((n*2) + 1), 2):
 suma = suma + i
if i == 10 + n*2 - 1:
   print(suma)
# zad 8
n = int(input("kwota wejściowa: "))
lat = int(input("ile lat: "))
miesiace = lat/12
for i in range(lat, lat + 1):
  print(n + n*((6*i)/100))
zad 9
n = int(input("liczba: "))
n = n * 100
for i in range(21, n, 100):
  print(i)
# zad 10
import math
a = 0
for i in range(1, 1000):
  if i % 10 == 0: 
    a = i
  elif i - a == math.sqrt(i):
    print(i)
  
   
    
