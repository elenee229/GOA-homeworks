#5) დაწერეთ ფუნქცია, რომელიც იღებს ლექსიკონს და აბრუნებს მის keys-სა და values-ს .keys() და .values() მეთოდებით. დაბეჭდეთ ორივე შედეგი და დაურთეთ კომენტარები
def dict1(dict2):
    keys=dict2.keys()#returns dictionary keys
    values=dict2.values()#returns dictionary values

    print(keys)
    print(values)
    return keys,values
