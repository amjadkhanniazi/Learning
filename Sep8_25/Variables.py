name="alice"
age=23
height=5.9
is_student=False
lists=["Python","HTML"]
dicts={"Atr1":"img1","Atr2":"img2"}

templateA=f"her name is {name}. she is {age} years old"
templateB="she is {0}, She is {1} feet.".format(name, height)
# print(templateB)

#Loops
for num in lists:
    print(f"Learning {num}")
