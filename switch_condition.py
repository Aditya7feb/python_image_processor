def switch():
    r = int(input("Enter Radius : ")) # it takes user input
    h = int(input("Enter Height : ")) # it takes user input

# This will guide the user to choose option
    print("Press 1 for Surface Area\n press 2 for Literal Area \n press 3 for Volume ")

# This will take option from user    
    option = int(input(" your option : "))

# Calculate Surface Area Of Cylinder
    def Sar():
        result = 2*3.17*r*(r+h)
        print(" Surface Area Of Cylinder = ",result)

# Calculate Literal Area Of Cylinder
    def Lar():
        result = 2 * 3.17 * r * h
        print("Literal Area Of Cylinder = ", result)

# Calculate Volume Of Cylinder
    def vol():
        result = 3.17*r*r*h
        print("Volume Of Cylinder = ", result)

# If user enters invalid option then this method will be called 
    def default():
        print("Incorrect option")

# Dictionary Mapping
    dict = {
        1 : Sar,
        2 : Lar,
        3 : vol,

    }
    dict.get(option,default)()