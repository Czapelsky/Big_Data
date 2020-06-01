import random

def get_triangle(x):
    return x*x*x
    
for i in range(50):
    x = random.randint(1, 1000)
    tri = get_triangle(x)
    print(x, tri)