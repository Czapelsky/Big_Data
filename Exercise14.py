slownik= {"item 1": 45.50, "item 2":35, "item 3": 41.30, "item 4":55, "item 5 ": 24}#slownik

for i in range(3):
    max_val = 0
    key = "zledane"
    for k, v in slownik.items():#metoda items - pozwala na iteracje dla par klucz- wartosc, kolejnosc fora ma znaczenie, pierwsza zmienna jest stringiem, druga zas przupisanu mu wartoscai w slowniku
        if v > max_val:
            max_val = v
            key = k
    print(key, slownik[key])
    del slownik[key]# konstrukcja ta wyrzuca nie tylko indeks, ale tez wartosc, poniewaz w slowniku nie moze istniec wartosc bez indeksu