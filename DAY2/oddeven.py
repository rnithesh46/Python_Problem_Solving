number=[]
n=int(input("enter how many number you want to enter: ."))
for i in range(n):
    num=int(input("enter the number: "))
    number.append(num)
even=0
odd=0
for num in number:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)