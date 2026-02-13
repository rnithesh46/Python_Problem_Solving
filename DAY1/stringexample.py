# s=input("enter the string: ")
# result=s.replace(" ","")
# print(result)

s=input("enter the string: ")
length=len(s)
mid=length//2
s1=s[:mid]
s2=s[mid:]
fname=s1[::-1]
lname=s2[::-1]
result=fname+lname
print(result)