#3) შექმენით ფუნქცია manual_count, რომელიც მიიღებს სიას და ელემენტს და დააბრუნებს ელემენტის რაოდენობას სიაში. გამოიყენეთ მხოლოდ loop და if, .count მეთოდის გარეშე
def manual_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count