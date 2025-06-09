#12) დაწერე ფუნქცია, რომელიც იღებს სიტყვების სიას და აბრუნებს სიის ყველაზე გრძელ სიტყვას. გამოიყენე ციკლი და 'len()' შედარებისთვის
def list(words):
    word2="" 
    for word in words:
        if len(word)>len(word2):
           word2=word
    return word2
    
print(list(["carrotinbasket","broccoli","kiwi","mango222222222222222222"]))    