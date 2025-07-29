#4) შექმენით სიები fruits, colors, numbers. თითოეულზე გამოიყენეთ index, count, sort, sorted, min, max მეთოდები & ფუნქციები და დააკომენტარეთ თითოეული მაგალითი (რას აკეთებს)
fruits=["apple","banana","blueberry","kiwi","apple","kiwi"]
colors=['red', 'pink','blue','purple','orange','red','pink']
numbers=[1,3,5,65,43,21,33,6,5,6]

print(fruits.index('kiwi'))
print(colors.index('red'))
print(numbers.index(3))
#index finds the place of the element in the list

print(fruits.count('apple'))
print(colors.count('pink'))
print(numbers.count(6)) 
#count finds how many times is element repeated in list

colors.sort()
print(colors)

numbers.sort()
print(numbers)

fruits.sort()
print(fruits)
#sort sorts the elements in list

sorted_fruits=sorted(fruits)
print(sorted_fruits)

sorted_numbers=sorted(numbers)
print(sorted_numbers)

sorted_colors=sorted(colors)
print(sorted_colors)
#sorted makes new list

print(min(fruits))
print(min(numbers))
print(min(colors))
#min returns first element in list

print(max(fruits))
print(max(numbers))
print(max(colors))
#max returns last element in list




