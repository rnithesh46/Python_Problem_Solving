def PartySuccessCheck(day,attendees):
    days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
    #Input constraints
    if day not in days:
        return "Invalid Input"
    if attendees<0:
        return "Invalid Input"
    
    if day in ["FRI","SAT","SUN"]:
        if attendees>1500:
            return "Successfull"
        else:
            return "Unsuccessfull"
    else:
        if 700<=attendees<=1000:
            return "Successfull"
        else:
            return "Unsuccessfull"

#main()
day=input("Enter the day of the week: ").strip().upper()
attendees=int(input("Enter the number of attendees: ").strip())
print(PartySuccessCheck(day,attendees))