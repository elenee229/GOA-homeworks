#5) შექმენით ფუნქცია რომელიც მიიღებს x და y კორდინატს, შემდეგ კი გადაცემული კორდინატების ადგილას დახაზავს კვადრატს, დავალების შესასრულებლად გამოიყენეთ მოდული: from turtle import *
from turtle import *

def square(x,y):
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(200)
        right(90)

square(0,0)        

exitonclick()    