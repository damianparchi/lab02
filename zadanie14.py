import math
n = int(input("enter a number: "))
num_sqrt = n **0.5
if(n<0):
    print('liczba ujemna')
else:
    print("Pierwiastek z liczby {} to {}".format(n,num_sqrt))