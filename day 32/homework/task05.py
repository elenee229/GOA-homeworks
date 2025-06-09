#6) დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს
def av(num):
    if len(num)==0:
        return 0
    else:
        return sum(num)/len(num)
print(av([112,43,12]))    