import sys


iphone = 3000
print('Ile masz pieniędzy?')

try:
    money = int(input())
except ValueError:
    print('Wprowadzono niepoprawną kwotę')
    sys.exit()

print('Aktualna cena iPhoneX = ', iphone)
if iphone > money:
    print('Brakuje Ci ', iphone - money, 'aby nabyć iPhoneX')
else:
    print('Stać Cię na ', money / iphone, 'iPhoneX')