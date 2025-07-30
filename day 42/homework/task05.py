#6) შექმენით ლექსიკონი person და გამოიყენეთ .items() მეთოდი, რათა დაბეჭდოთ ყველა key და value წყვილად. გამოიყენეთ loop და კომენტარი დაუმატეთ შედეგს
person={
    'name': 'ele', 
    'age': 100,
    'hobby': 'nun'
}
def person1(person):
    for key,value in person.items():
        print(f"{key} ,{value}")