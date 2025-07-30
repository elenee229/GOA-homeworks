#3) სიტყვების სიიდან "words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']" შეარჩიეთ მხოლოდ ისინი, რომლების სიგრძე მეტია 5-ზე, ჯერ "for"-ით, შემდეგ list comprehension-ით
words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
long_words=[]
for word in words:
    if len(word)>5:
        long_words.append(word)
print(long_words)        