#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output in the following format.
#The total amount is ______.

#defining function
def getapp():
    apple= int(input("How many apples do you want to buy? "))
    return apple

def getOrgs():
    orange= int(input("How many orange do you want to buy? "))
    return orange

def getPrice(apple, orange):
    apple_price= apple * 20
    orange_prize= orange *25
    total = apple_price + orange_prize
    return total

#step 
apples = getapp()
oranges = getOrgs()
totalprice = getPrice(apples, oranges)

print(f"The total amount is {totalprice}.")
