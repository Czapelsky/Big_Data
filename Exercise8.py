print("Podaj słowo do rotacji: ")
word = input()
word_list = list(word)
for i in range(len(word_list)):
    as_number = ord(word_list[i])+1
    as_char = chr(as_number)
    word_list[i] = as_char
word_rotated = "".join(word_list)
print(word_rotated)