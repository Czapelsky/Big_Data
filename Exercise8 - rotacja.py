print("Podaj słowo do rotacji: ")
word = input()
word_list = list(word)# zamienia slowo stringowe w tablice
for i in range(len(word_list)):#zczytanie dlugosci tablicy
    as_number = ord(word_list[i])+1# zamiana pojedynczego znaku na liczbe,
    as_char = chr(as_number)#zmienia liczbe na znak
    word_list[i] = as_char
word_rotated = "".join(word_list)# zbiera wszystkie litery podzielone uprzednio na tablice i laczy w calosc, tak naprawde po kazdej zmiennej z world_list wstawia pusty znak
print(word_rotated)