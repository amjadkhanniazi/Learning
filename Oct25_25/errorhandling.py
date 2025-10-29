def division_funct(num1, num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    finally:
        print("Execution of division_funct is complete.")


print(division_funct(10, "0"))


def validate_email(email):
    try:
        if "@" not in email:
            raise ValueError("Invalid email format")
        return {"Valid": True, "Email": email}
    except ValueError as ve:
        return{"Valid": False, "Error": str(ve)}

var2=validate_email("userexample@gmail.com")
print(f"Status: {var2["Valid"]}, Info:{var2["Email"]}")