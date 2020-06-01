items = {"item 1": 45.50, "item 2":35, "item 3": 41.30, "item 4":55, "item 5 ": 24}

for i in range(3):
    max_val = 0
    key = "zledane"
    for k, v in items.items():
        if v > max_val:
            max_val = v
            key = k
    print(key, items[key])
    del items[key]