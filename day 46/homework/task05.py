#6) სიიდან "animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']" შექმენით ახალი სია, რომელიც შეიცავს სიტყვების პირველ ასოებს, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ აირჩიეთ მხოლოდ ის სიტყვები, რომლებიც "e"-ზე იწყება
animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
new_list=[]
for animal in animals:
    new_list.append(animal[0])
print(new_list)    