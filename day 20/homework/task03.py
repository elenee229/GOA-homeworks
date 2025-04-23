#4) შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები

even = 0
odd = 0

number = int(input("Enter a number:"))

while number>= 0:
    if number % 2 == 0:
        even+= 1
    else:
        odd+= 1

    number = int(input("Enter other number: "))
    print("odd numbers ",odd)
    print("even numbers ",even )
