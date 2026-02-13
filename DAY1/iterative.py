N=input("Enter the number: ")
if len(N)!=4 or not N.isdigit():
    print("Invalid input. Please enter a 4-digit number.")
else:
    increasing = True
    decreasing = True
    for i in range(3):
        if N[i] >= N[i+1]:
            increasing = False
        if N[i] <= N[i+1]:
            decreasing = False
    if increasing:
        print("Fancy number")
    elif decreasing:
        print("Fancy number")
    else:
        print("Not fancy number")