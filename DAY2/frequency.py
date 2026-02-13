num_series=input("Enter the list of numbere series:").split()
k=int(input("Enter the threshold\n"))
processed_num=[]
print("the number with frequ > k")
for num in num_series:
    if num not in processed_num:
        count=0
        for i in num_series:
            if i==num:
                count+=1
        if count>k:
            print(f"Number {num}:{count} times")
        processed_num.append(num)