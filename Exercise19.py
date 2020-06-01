import random
import time
import numpy# biblioteka dla ciezkich matematycznych zadan

print("Podaj rozmiary macierzy")
print("M:")
M = int(input())
print("N:") 
N = int(input())

start = time.time()#metoda zczytujaca aktualny czas

matrix_1 = numpy.random.randint(1, 14, (M,N))#tworzy macierz o ksztalcie MxN, M oraz N to tuple,i zapelnia ja ranodmowymi wartosciami 1-14
matrix_2 = numpy.random.randint(1, 14, (M,N))
matrix_suma = matrix_1 + matrix_2#mozemy dodawac bezposrednio macierze dzieki bibliotece numpy

end = time.time()

print(matrix_1)
print(matrix_2)
print(matrix_suma)
print("Czas działania programu: ", end - start)

