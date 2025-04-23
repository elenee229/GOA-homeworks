#2) შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს, შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით, თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ "The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."
num=int(input("enter your number: "))
if num>0:
    if num % 2 == 0:
        print("the number is positive and even")
    else:
        print("the number is positive and odd")
elif num < 0:
    print("The number is negative.")
else:
    print("the number is zero")
