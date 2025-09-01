def CarPrice(age):
    # ford freestyle x,y,z,a,b,c - age is 1
    if age == 1:
        print ("18000")
    elif age == 1:
        print ("17950")
    elif age == 1:
        print ("17900")
    elif age == 1:
        print ("18100")
    elif age == 2:
        print ("16000")
    elif age == 3:
        print ("14000")
    elif age == 4:
        print ("12000")
    elif age == 5:
        print ("10000")
    else:
        print ("Unknown age")
age = int(input("Enter the age of the car (1-5): "))
CarPrice(age)

# New car - fixed price
# Used Car - Depreciation, change every car / 