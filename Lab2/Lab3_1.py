a = int(input('Liczba 1: '))
b = int(input('Liczba 2: '))
print('Wejście', a,', ', b)
if a > b:
    (a,b)=(b,a)
while a <= b:
    print(a, end=' ')
    a += 1