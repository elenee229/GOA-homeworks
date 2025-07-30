#2) შექმენით set სახელად numbers, დაამატეთ მას ორი რიცხვი add() მეთოდით და წაშალეთ ორი ელემენტი remove() მეთოდით. შემდეგ შექმენით მეორე set სახელად even_numbers და გამოიყენეთ union(), intersection(), difference() ორივე set-ზე. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი
numbers={2,3,5,67,53,21}
numbers.add(44)
numbers.add(122)
print(numbers)
numbers.remove(2)
numbers.remove(122)
print(numbers)
even_numbers={2,4,22,56,78,100}
#union merges sets
union_numbers=numbers.union(even_numbers)
print(union_numbers)
#intersection tells the same elements in sets 
intersection_numbers=numbers.intersection(even_numbers)
print(intersection_numbers)
#difference tells the different between sets
difference_numbers=numbers.difference(even_numbers)
print(difference_numbers)