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
for i in range(1, n+1):  # petla for, od 1 do podanej wartości +1 wykonuje // wartość prawa jest wyższa o 1 niż faktycznie powinna być, ponieważ nie jest ona liczona.
    factorial = factorial*i   # instrukcja dla silni

print(factorial)