#5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები
pin="1111"

attempts=3

while attempts>0:
    pin1=input("enter your pin:")

    if pin1==pin:
        print("access granted")
        break
    else:
        attempts-=1
        if attempts>0:
            print(f"incorrect pin you have {attempts} attempts left")
        else:
            print("can't get in")