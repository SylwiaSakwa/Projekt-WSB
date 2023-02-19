# Zdefiniuj funkcję, która będzie pobierała dwie wartości liczbowe i zwracała sumę tych wartości 

def sum (arg1, arg2):
    return arg1 + arg2
print (sum(2, 3))

# Zdefiniuj funkcję, która będzie pobierała dwie wartości liczbowe i zwracała sumę oraz różnicę tych wartości w jednym poleceniu return

def sum_diff (arg1, arg2):
    return arg1 + arg2, arg1 - arg2
print (sum_diff(5,3))

# Zdefiniuj funkcję, która pobierze jedną wartość liczbową i wykona takie założenia: jeśli zostanie przekazana wartość argumentu podczas odwołania się do funkcji, to zwraca kwadrat tej liczby, jeśli nie zostanie przekazana żadna wartość do funkcji, to zwraca liczbę 0 (zero)(zastosuj instrukcję warunkową if)

#1 sposób
def pow(arg=None):
    if arg is not None:
        return arg**2
    else:
        return 0

print(pow())
print(pow(3))

#2 sposób
def pow(arg="hello"):
    if arg != "hello":
        return arg**2
    else:
        return 0
    
print(pow())
print(pow(3))


    
