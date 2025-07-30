#5) სიიდან "mixed = [2, 5, 8, 11, 14, 17, 20]" შექმენით ორი სია list comprehension-ით: ერთში მხოლოდ ლუწები, მეორეში — კენტები
mixed = [2, 5, 8, 11, 14, 17, 20]
list1=[]
list2=[]
for num in mixed:
 if num % 2 ==0:
    list1.append(num)
 else:
    list2.append(num) 
print(list1)
print(list2)