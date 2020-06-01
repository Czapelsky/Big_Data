import sys

print("Podaj liczbę")
try:
    print('n = ')
    n = int(input())
except ValueError:
    print('Wprowadzono niepoprawną liczbę')
    sys.exit()
    
for i in range(1, n+1, 1): 
    if (n % i==0) : 
        print(i)