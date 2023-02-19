#Stwórz instrukcję, która będzie zwracała informację czy liczba jest parzysta czy też nieparzysta
liczba = 1

if  liczba % 2 == 0:
    print(liczba, " jest liczbą parzystą")
else:
    print(liczba, " jest liczbą nieparzysta")

#Stwórz instrukcję, która porówna do siebie dwie zmienne posiadające wartości liczbowe -wskaże czy liczba jest równa, mniejsza czy większa od drugiej

liczba1 = 7
liczba2 = 6

if liczba1 == liczba2:
    print("Liczby są takie same")
elif liczba1 > liczba2:
    print("Liczba1 jest większa niż Liczba2")
else:
    print ("Liczba2 jest większa od Liczba1")