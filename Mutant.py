import random
import string

def count(s):# funkcja bedzie wywolana dla konkretnej zmiennej
    sum = 0
    for c in s:
        sum += ord(c)# zamiana  znaku stringowego w liczbe w kodzie ASCII
    return sum

def generate_file():
    file = open("mutant.txt", "a+")# A dodawanie, + jesli nie ma takiego pliku to go tworzy
    for _ in range(300):
        s = "".join(random.choice(string.ascii_uppercase) for _ in range(50))# 50 RANDOMOWYCH WYBOROW Ze stringa ASCII (drukowanych)
        file.write(s)
        file.write("\n")
    file.close()
    
def count_file():
    file = open("mutant.txt", "r")
    fl = file.readlines()# pozwala na literowanie pliku, ale po wierszu
    for l in fl:
        print(l, count(l))
        
generate_file()
count_file()


