# Wypisz liczby od 1 do 10 za pomocą pętli FOR

for i in range (1, 11):
    print (i)

c=1
while c <= 10:
    print(c)
    c += 1

# dodanie do listy
suma_lista = []
for d in range (1, 11):
    suma_lista.append(d)

print(suma_lista)


# Ciąg Fibonacci - wyświetl za pomocą pętli kolejne numery ciągu Fibo od 0 do 10 elementu
# Ciąg Fibonacciego – ciąg liczb naturalnych określony rekurencyjnie w sposób następujący: Pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich.

# pętla while

liczba1 = 0
liczba2 = 1

print(liczba1)
print(liczba2)

iteracja = 0

while iteracja < 11:
    kolejna_liczba = liczba1 + liczba2
    liczba1 = liczba2
    liczba2 = kolejna_liczba

    print(kolejna_liczba)

    iteracja += 1



a = 0
b = 1

for i in range (13):
    print(a)
    a, b = b, a + b
