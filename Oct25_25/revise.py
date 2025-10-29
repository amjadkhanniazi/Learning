def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))


def form_data(name, age):
    if not name or age<=0:
        if not name:
            return "Name is required."
        if age<=0:
            return "Age must be a positive number."

    return {
        "status": "success",
        "data": {
            "name": name,
            "age": age
        }
    }

var1=form_data("Alice", 25)
print(f"Name: {var1["data"]["name"]}, Age: {var1["data"]["age"]}")