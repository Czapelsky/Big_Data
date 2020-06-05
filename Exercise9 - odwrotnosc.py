print("Wprowadź słowo do odwrócenia: ")
word = input()
word_list = list(word)# zamiana stringa na tablice, dzieki temu kazda litera ma oddzielną kolumnę
word_list.reverse()#odwrocenie liter w tablicy
print("".join(word_list))