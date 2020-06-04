print("Podaj ścieżkę do pliku:")
path = input()
try:
    file = open(path, "r+")
except FileNotFoundError:
    print("Plik nie istnieje")
    exit()

data = file.read()
file.close()
new_data_list = []
data_list = list(data)
for d in data_list:
    as_number = ord(d)+1
    as_string = chr(as_number)
    new_data_list.append(as_string)
    
new_data = "".join(new_data_list)
file = open(path, "w")
file.write(new_data)
file.close()
