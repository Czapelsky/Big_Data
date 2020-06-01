data = {":)": "😃", ":(": "😞"}

def print_emoji(x):
    print(data[x])

print("Podaj emotkę: ")
x = input()
print_emoji(x)