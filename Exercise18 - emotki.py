data = {":)": "😃", ":(": "😞"}

def print_emoji(x):
    print(data[x])

print("Podaj emotkę: ")
x = input()
if x not in data:
    print('slownik nie posiada takiej emotki')
else:
    print_emoji(x)
