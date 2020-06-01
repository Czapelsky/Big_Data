data = [1, 3, 5, 6, 3, 5, 6, 1, 3, 8, 9 , 1, 5]
result = []
for i in data:
    if i not in result:
        result.append(i)
print(result)
        