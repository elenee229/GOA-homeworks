#2) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ თუ ეს რიცხვი დადებითია დაბეჭდეთ ეს და კიდევ შეამოწმეთ ლუწია თუ კენტი, ხოლო თუ არაა დადებითი მხოლოდ დაბეჭდეთ რომ უარყოფითია
num=int(input("enter your number:"))
if num>0:
    print("number is positive")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")  

else:
    print("number is negative")  