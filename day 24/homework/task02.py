#3) შექმენით სიტყვების სია, შემდეგ მის შემობრუნებულ ვერსიას გადაუარეთ for ციკლით, დაბეჭდეთ ყოველი მეორე ელემენტი (რომ გაიგოთ ყოველი მეორე აიღეთ ცვლადი რომელიც თავიდან 0 იქნება, ყოველ გამეორებაზე კი გაზრდით ერთით და შეამოწმეთ ლუწია თუ კენტი)
fruits=["apple","watermelon","strawberry","blueberry","raspberry","melon","banana","kiwi"]
fruits1=fruits[::-1]
fruits2=0
for fruits in fruits1:
    if fruits2 % 2 == 0:
        print(fruits)
    fruits2+=1