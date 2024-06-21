def cal():
    while True:
        print("Basic Arithmetic operations ") 
        print("1.Addition")
        print("2.Subttraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("Enter any number where !(1-5) for Exit")
        a=int(input("Enter operation in between(1-5): "))
        if a not in range(1,6):
            print("Exiting the calculator. Goodbye!")
            break
        try:
            b=float(input("Enter the First number: "))
            c=float(input("Enter the Second number: "))
        except valueError:
            print("Invalid Input, Please enter valid number!")
            continue
        if a==1:
            result=b+c
            print("Addition of values",b,"+",c,'=',result)
        elif a==2:
            result=b-c
            print("Subtraction of values",b,"-",c,'=',result)
        elif a==3:
            result=b*c
            print("Multiplication of values",b,"*",c,'=',result)
        elif a==4:
            result=div(b,c)
            print("Division of values",b,"/",c,'=',result)
        elif a==5:
            result=b%c
            print("Modulus of values",b,"%",c,'=',result)
        else:
            print("Please enter valid numberin range(1-6)")
def div(b,c):
    try:
        result=b/c
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please try again.")
        return None
cal()
