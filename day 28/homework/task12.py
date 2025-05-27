#13) შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა input-ით. თუ სიტყვა მოიძებნება find-ით, დაბეჭდეთ პოზიცია, სხვა შემთხვევაში კი დაბეჭდეთ word not found
string="bla ble bli blo blu "
word=input("enter a word:")

word1=string.find(word)

if word1 != -1:
    print("word was found")
else:
    print("word not found")