class multipleFunctions():
    def oddEven():
        num=int(input("Enter a number"))
        if(num%2==0):
            print("Even Number")
            message="It is Even Number"
        else:
            print("Odd Number")
            message="It is Odd Number"
        return message

    def BMI():
    #Body Mass Index
        weight = float(input("Enter the BMI Index:"))
        if(weight < 18.5):
            print("Underweight")
            message="Under Weight"
        elif((weight >= 18.5) and (weight <= 24.9)):
            print("Normal range")
            message="Normal range"
        elif((weight >= 25.0) and (weight <= 29.9)):
            print("Overweight")
            message="Over Weight"
        else:
            print("Very Overweight")
            message="Very Over Weight"
        return message

    def Elegible():
            gender = input("Your Gender:")
            age = int(input("Your Age:"))
            if(gender == 'Male'):
                if(age >=21 ):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")
            elif(gender == 'Female'):
                if(age >=18 ):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")

    
    def Subfields():
            print("Sub-fields in AI are:")
            print("Machine Learning")
            print("Neural Networks")
            print("Vision")
            print("Robotics")
            print("Speech Processing")
            print("Natural Language Processing")

    def percentage():
            Subject1= int(input("Subject1="))
            Subject2= int(input("Subject2="))
            Subject3= int(input("Subject3="))
            Subject4= int(input("Subject4="))
            Subject5= int(input("Subject5="))
            Total = Subject1+Subject2+Subject3+Subject4+Subject5
            Percentage = (Total/500)*100
            print("Total : ",Subject1+Subject2+Subject3+Subject4+Subject5)
            print("Percentage : ",Percentage) 

    def triangle():
            Height = int(input("Height:"))
            Breadth = int(input("Breadth:"))
            AreaTriangle = (Height*Breadth)/2
            print("Area formula: (Height*Breadth)/2")
            print("Area of Triangle:",AreaTriangle)
            Height1 = int(input("Height1:"))
            Height2 = int(input("Height2:"))
            Breadth = int(input("Breadth:"))
            PerimeterTriangle = Height1+Height2+Breadth
            print("Perimeter formula: Height1+Height2+Breadth")
            print("Perimeter of Triangle:",PerimeterTriangle)
