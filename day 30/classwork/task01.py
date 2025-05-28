#1) თითოეულ მეთოდზე: len, append, insert, pop, remove მეთოდებზე გააკეთეთ 3-3 მაგალითი. len ფუნქციაზე მოიყვანეთ string-ის მაგალითიც

numbers=[20,12,45,52,88]
numbers.append(12)
print(numbers)
numbers.append(52)
print(numbers)
numbers.append(20)
print(len(numbers))

numbers.insert(2 , 33)
print(numbers)
numbers.insert(5 ,55)
print(numbers)
numbers.insert(0,123)
print(len(numbers))

numbers.pop(2)
print(numbers)
numbers.pop(0)
print(numbers)
numbers.pop(4)
print(len(numbers))

numbers.remove(88)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.remove(33)
print(len(numbers))