import os
def save_user_data(filename, user_data):

    try:
        with open(filename, 'a') as file:
            for user in user_data:
                file.write(f"{user["name"]},{user["age"]},{user["email"]}\n")
        return True
    except IOError:
        return False

def load_user_data(filename):
    users= []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, age, email = line.strip().split(',')
                users.append({"name": name, "age": int(age), "email": email})
        return users
    except FileNotFoundError:
        return []


# var = save_user_data("users.txt", [{"name": "Alice", "age": 23, "email": "domael"}])
# print(var)

var = load_user_data("users.txt")
for user in var:
    print(f"Name: {user["name"]}, Age: {user["age"]}, Email: {user["email"]}")