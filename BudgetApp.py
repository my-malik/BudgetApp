from budgetClass import Budget

food = Budget(float(input("Enter starting balance for food:£")))
print(f"food: {food}")
print()

withdrawFood = (float(input("Enter how much you want to withdraw for food:£")))
print(food.withdraw(withdrawFood))
print()

depositFood = (float(input("Enter how much you want to deposit for food:£")))
print(food.deposit(depositFood))
print()

clothing = Budget(float(input("Enter starting balance for clothing:£")))
print(f"clothing:{clothing}")
print()

withdrawClothing = (float(input("Enter how much you want to withdraw for clothing:£")))
print(clothing.withdraw(withdrawClothing))
print()

depositClothing = (float(input("Enter how much you want to deposit for clothing:£")))
print(clothing.deposit(depositClothing))
print()



depositToClothing = (float(input("How much to transfer from food to clothing:£")))
clothing.transferIn(depositToClothing)
food.transferOut(depositToClothing)
print(f"food: {food}\nclothing: {clothing}")


depositToFood= (float(input("How much to transfer from clothing to food:£")))
food.transferIn(depositToFood)
clothing.transferOut(depositToFood)
print(f"food: {food}\nclothing: {clothing}")














