#14) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მასში ხმოვნების (a, e, i, o, u) რაოდენობას. გამოიყენე ციკლი და if-else
def vowels1(sen):
    count=0
    vowels="aeiouAEIOU"
    for char in sen:
        if char in vowels:
            count +=1

    return count
print(vowels1(input("enter your sentence:")))