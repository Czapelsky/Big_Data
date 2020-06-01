import random

data = []
for i in range(100):
    rnd = random.randint(1, 100)
    data.append(rnd)
    
count = 0   
for number in data:
    if number < 23:
        count += 1
        
print(data)
print(count)