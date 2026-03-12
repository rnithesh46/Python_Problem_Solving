n=int(input("n = "))
target=int(input("target = "))
# linear search
for i in range(1,n+1):
    if i==target:
        print(f"linear_steps: {i}")
        break

# binary search
binary_steps=0
low=1
high=n
while low<=high:
    binary_steps+=1
    mid=(low+high)//2
    if mid==target:
        break
    elif mid<target:
        low=mid+1
    else:
        high=mid-1
print("Binary Steps:",binary_steps)