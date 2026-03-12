n=int(input("n = "))
print("Total:",n)
for i in range(1,n+1):
    print(i,end=" ")
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"({i},{j})",end=" ")