import math

option =input("Choose an option: Bond or Investment \n")

if option == "Bond" or option == "bond" or option == "BOND":
    house = int(input("please enter the value of your home\n"))
    Rate = int(input("please enter your interest rate\n"))
    time = int(input("how many months are you going to need to pay the bond?\n"))
    p = (house)
    i = (Rate)
    n = (time)
    x = (i*p)/(1-(1+i)**(-n))
    print(x)

elif option == "investment" or option == "Investment" or option == "INVESTMENT":
    amount = int(input("please enter amount of money you are deposting \n"))
    rate = int(input("please enter the interest rate \n"))
    invest = int(input("please the amount of years you would like to invest for \n"))
    interest = input("please select simple or compound \n")
    r = rate/100
    P = amount
    t = invest
    if interest == "simple":
        a = P*(1+r*t)
        print(a)
    elif interest == "compound":
        A = P*math.pow((1+r),t)
        print(A)



    







