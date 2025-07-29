#7) დაწერეთ ფუნქცია tuple_info, რომელიც მიიღებს tuple-ს და დაბეჭდავს მის სიგრძეს, პირველ და ბოლო ელემენტს
def tuple_info(tup):
    length=len(tup)
    first_element = tup[0] if length > 0 else None
    last_element = tup[-1] if length > 0 else None

    print(f"Length: {length}") 
    print(f"first element: {first_element}")
    print(f"Last element: {last_element}")