import sys

print('Wprowadź liczbę:')
try:
    print('n = ')
    n = int(input())
except ValueError:
    print('Wprowadzono niepoprawne dane')
    sys.exit()
    
if (n<0):
    print('Nie można wyliczyć silni')
    sys.exit()
    
if (n==0):
    print(1)
    sys.exit()

factorial = 1
for i in range(1, n+1):
    factorial *= i

print(factorial)