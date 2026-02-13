product=eval(input("Enter the dictionary: "))
sort_by=input("key or price: ").strip().lower()
if sort_by=='key':
    sorted_dict=sorted(product.items())
elif sort_by=='price':
    sorted_dict=sorted(product.items(), key=lambda x: x[1])
else:
    sorted_dict=product
    print("Invalid input")
print("Sorted dictionary:",sorted_dict)
# dict={'Laptop':800,'Mobile':400,'TV':600,'Headphones':100}