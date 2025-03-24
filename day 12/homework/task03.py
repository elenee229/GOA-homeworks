#4) შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები

temperature= 35
cloudy="true"
exam=100
passgrade=70
kids_passed=20
not_passed=19


print(temperature>30 and not cloudy) #false
print(temperature>30 or  cloudy) #true
print(exam>99 and passgrade<71)#true
print(exam>99 or passgrade>71)#true
print(exam<passgrade or kids_passed>not_passed)#true
print(exam<passgrade and kids_passed>not_passed)#false