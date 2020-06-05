file = open('data.txt', 'r')# OTWIERA plik o konkretnej nazwie w tym samym folderze co plik, otwiera go do odczytu co oznacza 'r'
data = file.read()
count_C = data.count('C')
count_G = data.count('G')
part = (count_C+count_G)/len(data)
print('C+G stanowi ', part*100, '%')