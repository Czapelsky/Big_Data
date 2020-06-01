import random
import time

print("Podaj rozmiary macierzy")
print("M:")
M = int(input())
print("N:")
N = int(input())

start = time.time()

matrix_m, matrix_n, matrix_suma = [], [], []

for m in range(M):
    pomoc_m, pomoc_n = [], []
    for n in range(N):
        pomoc_n.append(random.randint(1, 14))
        pomoc_m.append(random.randint(1, 14))
    matrix_n.append(pomoc_n) 
    matrix_m.append(pomoc_m)
    
for m in range(M):
    temp = []
    for n in range(N):
        temp.append(matrix_m[m][n]+matrix_n[m][n])
    matrix_suma.append(temp)
    
end = time.time()
        
print(matrix_m)
print(matrix_n)
print(matrix_suma)
print("Czas wykonania: ", end-start)

