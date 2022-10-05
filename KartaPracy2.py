# # zad 1
# a = int(input("A:"))
# if a % 3 == 0:
#   print("Liczba jest podzielna przez 3")
# else:
#   print("Liczba nie jest podzielna przez 3")

# # zad 2

# a = int(input("A:"))
# if a >= 100 and a%17 == 0:
#   print("Wpisana liczba jest 3 cyfrowa i podzielna przez 17")
# elif a >= 100 and a%17 != 0:
#   print("Wpisana liczba jest 3 cyfrowa i nie podzielna przez 17")
# else:
#   print("Wpisana liczba nie jest 3 cyfrowa i podzielna przez 17")
# #zad 3
# wiek = int(input("Podaj wiek: "))

# if wiek >= 18:
#   print("Jesteś Pełnoletni")
# else:
#   print("Nie jesteś pełnoletni")
# #zad 4
# waga = int(input("Podaj ciężar pojazdu w kilogramach: "))
# if waga >= 20000:
#   print("Nie możesz przejechać")
# else:
#   print("Możesz przejechać")
# # zad 5
# a = int(input("liczba A:"))
# b = int(input("Liczba B:"))
# c = int(input("Podaj liczbę większą od A i mniejszą od B lub odwrotnie "))

# if c > a and c < b:
#   print("Dobrze!")
# elif c < a and c > b:
#   print("Dobrze!")
# else:
#   print("Źle")
# # zad 6
# p = int(input("liczba pierwsza: "))
# a = int(input("A:"))

# if ((a**p) - a) % p == 0:
#   print("Liczba p jest pierwsza")
# else:
#   print("Liczba p nie jest pierwsza ")
# # zad 7
p = int(input("Punkt początkowy: "))
s = int(input("Długość skoku: "))
k = int(input("Punkt końcowy: "))

if p + (s * 3) >= k:
  print("Żabka dotarła")
else:
  print("Żabka nie dotarła")