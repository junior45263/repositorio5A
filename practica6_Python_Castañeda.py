#PRACTICA 6 Bernardo Castañeda Rios 
import numpy as np

sample_list = [1, 2, 3]

array1 = np.array(sample_list)
print(array1)


#Vectores  arreglos undimensionales
my_vector = np.array(['arturo', 'samuel', 'carlos'])
#print(my_vector)


#Matrices arreglos bidimensionales 
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = np.array(my_matrix)
#print(matrix)
array2 = np.random.randint(0,10, size=(5,6))
#print(array2)

array3 = np.random.randint(0,100, size=(5,10))
print(array3)
print("La suma de los elementos del array es:  ", array3.sum())
print("La suma de las columnas es:  ", array3.sum(axis=0))
print("La suma de las filas es:  ", array3.sum(axis=1))

#Valor minimo y maximo de las columnas 
print("Valor maximo de las columnas es:  ", array3.max(axis=0))
print("Valor minimo de las columnas es:  ", array3.min(axis=0))

#Valor maximo y min de las filas
print("Valor maximo de las flas es:  ", array3.max(axis=1))
print("Valor minimo de las flas es:  ", array3.min(axis=1))

#Valor maximo y min de todo
print("La Valor maximo de todo es:  ", array3.max())
print("La Valor minimo de todo es:  ", array3.min())

#Creacion de rangos de numpy con el metodo arange
rango = np.arange(0,10)
#print(rango)

linspace = np.linspace(0,1,10)
#print(linspace)