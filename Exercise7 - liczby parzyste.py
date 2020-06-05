count = 0
print('Parzyste liczby:')
for i in range(1, 201):
    if (i%2) == 0:
        count+=1
        print(i)
print('Liczb parzystych było ', count)