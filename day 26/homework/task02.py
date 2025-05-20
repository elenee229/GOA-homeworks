fruits=["apple","strawberry","raspberry","banana","avocado","grapefruit","orange"]
favfruit=input("what's your favorite fruit")
fruit_in_basket=False
for fruit in fruits:
    if fruit==favfruit:
        fruit_in_basket = True
        break
    if fruit_in_basket:
        print("good choice")
    else:
        print("fruit not in basket")