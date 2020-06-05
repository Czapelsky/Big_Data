for number in range(2, 101):
    for i in range(2, number):
        if (number%i) == 0:
            break
    else:# wykonuje sie tylko wtedy gdy for przebiega bez zaklocen, ergo zostana wypisane tylko liczby pierwsze
        print(number)
