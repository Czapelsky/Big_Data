import math
import sys
        
print('Wprowadź dane do równania')

try:
    print('a = ')
    a = int(input())#input zawsze zczytuje stringa, dlatego jest w nawiasie, ponieważ potem jest zamieniany na zmienna intowa
    print('b = ')
    b = int(input())
    print('c = ')
    c = int(input())
except ValueError:
    print('Wprowadzono niepoprawne dane')
    sys.exit()

delta = b*b - 4*a*c

if delta < 0:
    print('Delta mniejsza od zera, brak rozwiązań')
    sys.exit()
    
x1 = (-b - math.sqrt(delta))/(2*a)#math.sqrt to pierwiastek
x2 = (-b + math.sqrt(delta))/(2*a)

print('x1 = ', x1)
print('x2 = ', x2)
