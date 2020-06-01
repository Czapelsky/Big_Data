import random
import time
import numpy

print("Podaj rozmiary macierzy")
print("M:")
M = int(input())
print("N:") 
N = int(input())

start = time.time()

matrix_m = numpy.random.randint(1, 14, (M,N))
matrix_n = numpy.random.randint(1, 14, (M,N))
matrix_suma = matrix_m + matrix_n

end = time.time()

print(matrix_m)
print(matrix_n)
print(matrix_suma)
print("Czas działania programu: ", end - start)

