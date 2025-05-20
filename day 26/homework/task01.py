#2) დაწერეთ პროგრამა, რომელიც ითხოვს ორ რიცხვს მომხმარებლისგან. შემოაყვანინეთ მომხმარებელს დაწყების და დასრულების რიცხვი. თუ მეორე რიცხვი ნაკლებია პირველზე, გამოუტანეთ შეტყობინება: არასწორი შუალედი. სხვა შემთხვევაში დაბეჭდეთ ყველა რიცხვი მოცემულ შუალედში ჩათვლით და იპოვეთ ამ რიცხვების ჯამი. გამოიყენეთ for ციკლი, if-else პირობა, input ფუნქცია, და int ტიპში გადაყვანა
num1=int(input("enter your started number:"))
num2=int(input("enter your ending number:"))

if num2<num1:
    print("wrong")
else:
    total=0
    print("range")
    for num in range(num1,num2 +1):
        print(num)
        total+=num
    print("the sum is",total)
    