def czy_palindrom(data):# Definicja funkcji czy_palindrom, gdzie bedzie onna przyjmowac zmienna data
    for i in range(len(data)):
        if data[i] != data[len(data)-i-1]:# ! strona lew rozna jest od prawej, sprawdzamy czy pierwa litera jest rozna od ostatniej
            return False
    return True

print("Podaj słowo do sprawdzenia: ")
data = input()
is_palindrome = czy_palindrom(data)

if is_palindrome:
    print(data, "to palindrom")
else:
    print(data, "to nie palindrom")



