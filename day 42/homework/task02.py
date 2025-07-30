#3) დაწერეთ ფუნქცია, რომელიც იღებს set-ს, ამატებს მას 3 ელემენტს add() მეთოდით, შემდეგ შლის ერთ ელემენტს remove() მეთოდით და აბრუნებს საბოლოო შედეგს
def n1_set(i_set):
    i_set.add(21)
    i_set.add(22)
    i_set.add(34)

    i_set.remove(34)

    return i_set