#4) რიცხვების სიიდან "nums = list(range(1, 21))" შექმენით ახალი სია კვადრატებით, ჯერ "for"-ით, შემდეგ list comprehension-ით. შემდეგ სცადეთ მსგავსი მაგალითი სხვა მოქმედებით
nums = list(range(1, 21))
new_list=[]
for num in nums:
    new_list.append(num**2)
print(new_list)    