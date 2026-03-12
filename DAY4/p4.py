def Recur_Sum(items,n):
    if n==0:
        return 0
    return items[n-1]+Recur_Sum(items,n-1)
items=[10,20,30,40,50]
print(Recur_Sum(items,5))
