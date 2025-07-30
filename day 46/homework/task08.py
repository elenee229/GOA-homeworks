#9) სთხოვეთ მომხმარებელს შეიყვანოს რიცხვი "input()"-ით და გადააკეთეთ "int"-ად. გამოიყენეთ "try" და "except", რომ გაუმკლავდეთ შეცდომას თუკი სიმბოლოები შეიყვანეს. დაბეჭდეთ „შეიყვანეთ მხოლოდ რიცხვი“
try:
   input1=input('enter your number:')
   number=int(input1)
   print(number)
except:
   print("enter only number:")

    