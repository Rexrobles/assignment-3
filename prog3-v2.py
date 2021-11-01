#prog3 using function

def getmoney():
    amountMoney= int(input("How much money do you have? "))
    return amountMoney

def getappPrice():
    appPrice= int(input("What is the price of an apple per piece? "))
    return appPrice

def getMaximumApple(money, price):
    MaximumApp= int(money//price)
    return MaximumApp

def getChange(money, price):
    change= money%price
    return change

#step
Amount_of_money= getmoney()
applePrice= getappPrice()
max_apples= getMaximumApple(Amount_of_money, applePrice)
total_change= getChange(Amount_of_money, applePrice)

print(f"you can buy {max_apples} apples and your change is {total_change} pesos.")