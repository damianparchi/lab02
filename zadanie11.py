n = int(input("Liczba wierszy: "))

for i in range(0,n):
    for j in range(0,n-i-1):
        print(end="")
    for j in range(1,2*i):
        print("*",end="")
    for j in range(0,n-i-1):
        print(end="")
    print()