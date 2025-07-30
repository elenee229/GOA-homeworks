#7) შექმენით ლექსიკონი animal, შექმენით მისი ასლი .copy() მეთოდით, შემდეგ კი გამოიყენეთ .clear() ორივეზე (დასაწყისში და ბოლოს დაბეჭდეთ ორივე ლექსიკონი, კომენტარით)
animal = {
        'dog': 'bark',
        'cat': 'meow',
        'pig': 'oink',
        'mouse': 'squik'
    }
print(animal)
copy1=animal.copy()
print(copy1)

animal.clear()
copy1.clear()
print(animal)
print(copy1)