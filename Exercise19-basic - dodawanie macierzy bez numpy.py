import random
import time

print("Podaj rozmiary macierzy")
print("M:")
M = int(input())
print("N:")
N = int(input())

start = time.time()

matrix_1, matrix_2, matrix_suma = [], [], []

for m in range(M):
    pomoc_1, pomoc_2 = [], []
    for n in range(N):
        pomoc_1.append(random.randint(1, 14))
        pomoc_2.append(random.randint(1, 14))
    matrix_1.append(pomoc_1) 
    matrix_2.append(pomoc_2)
    
for m in range(M):
    pomoc = []
    for n in range(N):
        pomoc.append(matrix_1[m][n]+matrix_2[m][n])
    matrix_suma.append(pomoc)
    
end = time.time()
        
print(matrix_1)
print(matrix_2)
print(matrix_suma)
print("Czas wykonania: ", end-start)

