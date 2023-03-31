class multipleFunctions():
    def add(s1,s2):
        addition = s1 + s2
        return addition
    def sub(s1,s2):
        subtraction = s1 - s2
        return subtraction
    def multiplication(s1,s2):
        mul = s1*s2
        return mul
    def division(s1,s2):
        div = s1/s2
        return div
    def OddEven(n):
        if(n%2!=0):
            print("The value is an odd number")
        else:
            print("The value is an even number")
    def Subfields():
            print("Machine Learning""\n","Neural Networks""\n","Vision""\n","Robotics""\n","Speech Processing""\n","Natural Language Processing""\n")
            print("The subfields in AI are:")
    def Gender_Eligibility():
        Gen = input("Your Gender: ")
        Age = int(input("Your age: "))
        if(Gen=="Male"):
            if(Age>=18):
                print("Not Eligible")
        if(Gen=="Female"):
            print("Eligible")
    def percentage():
        s1 = int(input("Subject1="))
        s2 =  int(input("Subject2="))
        s3 =  int(input("Subject3="))
        s4 =  int(input("Subject4="))
        s5 =  int(input("Subject5="))
        total = s1+s2+s3+s4+s5
        percent = total/5
        print("Total :",total,"\n","Percentage :",percent)    
    def triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        Area_Formula = (Height * Breadth)/2
        print("Area of a triangle: ", Area_Formula)
        Height_1 = int(input("Height 1: "))
        Height_2 = int(input("Height 2: "))
        Breadth_1 = int(input("Breadth: "))
        Perimeter_Formula = Height_1+Height_2+Breadth_1
        print("Perimeter of a triangle:", Perimeter_Formula)