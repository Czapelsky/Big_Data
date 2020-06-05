import sys

print("Podaj liczbę")
try:
    print('n = ')
    n = int(input())
except ValueError:
    print('Wprowadzono niepoprawną liczbę')
    sys.exit()

count=0

for i in range(1, n+1): 
    if (n % i==0) : # dzielenie naszej liczby, przez kolejne następujące po sobie liczby naturalne, gdzie wynikiem dzielenia jest reszta 0
        print(i)
        count = count + 1
print ('ilośc dzielników:', count)        