#3) შექმენით პროგრამა რომელიც მოხმარებელს შეეკითხება პაროლს სანამ სწორად არ ჩაწერს

password="elene1234"
user_entry=""
while user_entry != password:
    user_entry=input("enter your password:")
print("logged in successfully")