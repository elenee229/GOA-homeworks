#1) მოხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაუბეჭდეთ ეს რიცხვი დადებითია, უარყოფითი თუ ნეიტურალი ანუ ნული. შემდეგ კომენტარებით ახსენით რა გასნხვავებაა if-სა და elif-ს შორის რატომ არ შეიძლება ზოგერ elif-ს ნაცვლად if-ის გამოყენება
number=int(input("enter a number: "))
if number> 0:
    print("number is possitive")
elif number == 0:
    print("number is neutral")
else:
    print("number is negative")    
#elif is mix of else and if,elif command is only checked if "if" was false before    