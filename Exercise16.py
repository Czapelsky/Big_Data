def czy_palindrom(data):
    for i in range(len(data)):
        if data[i] != data[len(data)-i-1]:
            return False
    return True

print("Podaj słowo do sprawdzenia: ")
data = input()
is_palindrome = czy_palindrom(data)

if is_palindrome:
    print(data, "to palindrom")
else:
    print(data, "to nie palindrom")



