numbers=[1,2,3,4,5,6]

square=[x**2 for x in numbers]
square_condition=[x**2 for x in numbers if x%2==0]

# for sq in square_condition:
    # print(sq)


names=["alice", "bob", "max"]
upper_names=[name.upper() for name in names]
# print(upper_names)

words = ["hello", "world", "Lenght", "cat", "Dog"]
word_lenght=[len(word) for word in words]
# print(word_lenght)

long_words=[word for word in words if len(word)>3]
# print(long_words)

numberss=[1,-4,21,4,-8,0,3]
positive_numberss=[x**2 for x in numberss if x>0]
# print(positive_numberss)

text="abc123def456"
digit=[char for char in text if char.isdigit()]
# print(digit)

sentence="hello world python programming"
first_char=[word[0] for word in sentence.split()]
# print(first_char)

word="programming"
consonants=[char for char in word if char.lower() not in 'aeiou']
# print(consonants)

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

names=[student["name"] for student in students]
print(names)

grades=[student["grade"] for student in students if student["grade"]>80]
print(grades)