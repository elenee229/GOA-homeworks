#4) შექმენით dictionary სახელად student, დაამატეთ მას მონაცემები: name, hobby, height, weight. შემდეგ გამოიყენეთ .get() მეთოდი name-ის მისაღებად და .pop() მეთოდი height-ის წასაშლელად. დაუმატეთ კომენტარები, რას აკეთებს თითოეული მეთოდი
student = {
     
    "name": "sanny",
    "hobby": "playing",
    "height": 187,
    "weight": 85
}
#get return the specified value
name = student.get("name")
#pop pops out the element from dictionary
height = student.pop("height")
print(student)