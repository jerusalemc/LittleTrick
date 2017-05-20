import numpy as np

def f(n):
   a = np.zeros([n, n])
   for i in range(n):
       for j in range(i + 1):
           (row, column) = (i - j, j) if i % 2 else (j, i - j)
           a[row][column] = sum(range(i + 1)) + j + 1
           a[n - 1 - row][n - 1 - column] = n**2 + 1 - a[row][column] 
   return a       

if __name__ == '__main__':
   print(f(5)) 
