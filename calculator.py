def main():

    print("Number 1   =   ")
    num1 = float(input())
    print("Number 2   =   ")
    num2 = float(input())
    #the lines 3-6 take the input of the two numbers to be operated

    print("Choose The Opperation")
    print("Type 1 for Addition")
    print("Type 2 for Subbtraction")
    print("Type 3 for Multiplication")
    print("Type 4 for Division")
    operation = int(input())
    #the lines 9-14 ask the user to select the opperation

    if(operation==1):
        ans = num1 + num2
        ans2 = str(ans)
        num11 = str(num1)
        num22 = str(num2)
        print("The Sum of "+num11+" and "+num22+" = "+ans2)
    elif(operation==2):
        ans = num1 - num2
        ans2 = str(ans)
        num11 = str(num1)
        num22 = str(num2)
        print("The Difference of "+num11+" and "+num22+" = "+ans2)
    elif(operation==3):
        ans = num1 * num2
        ans2 = str(ans)
        num11 = str(num1)
        num22 = str(num2)
        print("The Product of "+num11+" and "+num22+" = "+ans2)
    elif(operation==4):
        ans = num1 / num2
        ans2 = str(ans)
        num11 = str(num1)
        num22 = str(num2)
        print("The Quotient of "+num11+" and "+num22+" = "+ans2)
    else:
        print("Dont Joke With Me !!")
    #the lines 17-42 give the answer of the equation

    print("Press 1 to Continue")
    print("Press 2 to Exit")
    con = int(input())
    if(con==1):
        main()
    elif(con==2):
        print("Thanks for using me")
    else:
        print("Dont Joke With Me !!")

main()
#the lines 45-53 decide the continuation of the code