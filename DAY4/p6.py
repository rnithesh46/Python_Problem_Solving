def climbing_stairs(n):
    if (n==0 or n==1):
        return 1
    return climbing_stairs(n-1) + climbing_stairs(n-2)

n=int(input("Enter the number of stairs: "))
print(climbing_stairs(n))