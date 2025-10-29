def Fruit_name(fruit1, fruit2):
    if fruit1=="Orange":
        status="fruit1 is Apple"
    else:
        status="fruit1 is not Apple"

    return f"{status}, and fruit2 is {fruit2}"

statement = Fruit_name("Apple", "Banana")
print(statement)

# def greet_user(name, greeting="Hello"):
#    return f"{greeting}, {name}!"

# user= greet_user("Amjad","Welcome Back")
# print(user)

def process_form_data(username,email,age=None):
    if not username or not email:
        return {"error":"username and email is required"}
    
    return {
        "success": True,
        "user":{
            "username": username,
            "email":email,
            "age":age
        }
    }

result= process_form_data("amjad","amjad@gmail.com", 23)

print(result)