file = open("lista.txt", "a+")
add_student = True
print("Podaj studentów do wczytania:")
students = []
while(add_student == True):
    print("Imie:")
    name = input()
    print("Nazwisko:")
    surname = input()
    print("Grupa:")
    group = input()
    student_data=(name, surname, group)
    students.append(student_data)
    print("Czy chcesz dodać kolejnego studenta? Wpisz tak/nie")
    dec = input()
    if dec == "nie":
        add_student = False
for s in students:
    student = ",".join(s)
    file.write(student)
    file.write("\n")
file.close()    

    