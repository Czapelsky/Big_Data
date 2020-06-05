def to_binary(a):
    if a is 0:
        return "0"
    result = []
    while(a>=1):
        result.append(str(a%2))#dodaje reszte z dzielenia podanej liczby przez 2 do tablicy result
        a = int(a / 2)
    result.reverse()#obracamy tablice dwojkowa
    return "".join(result)

print("Podaj liczbę:")
a = int(input())
a_binary = to_binary(a)
print(a, "w systemie dwójkowym to", a_binary)