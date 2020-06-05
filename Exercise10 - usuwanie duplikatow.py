data = [1, 3, 5, 6, 3, 5, 6, 1, 3, 8, 9 , 1, 5]
result = []#PUSTA TABLICA
for i in data:# dla kazdego elementu z tablicy
    if i not in result:# jesli tego elementu nie ma w tablicy
        result.append(i)# dodaj element
print(result)
        