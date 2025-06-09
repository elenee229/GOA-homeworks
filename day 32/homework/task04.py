#5) დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია
def num(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(num(int(input("enter your number:"))))
