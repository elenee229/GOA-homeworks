#6) მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო
num=0
num1=0

number=int(input("enter your number:"))

while number != -1:
    num += number
    num1 += 1
    number = int(input("Enter another number:"))
if num>0:
    mid = num / num1
    print("average:",mid)
else:
    print("nothing")