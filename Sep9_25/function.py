def sum(value1, value2=0):
    return value1+value2

# result=sum(5)
# print(result)

def mul(value1,value2):
    if value1==0 or value2==0:
        return "One of the value is Zero"
    return value1*value2

# result=mul(5,0)
# print(result)

def str_to_int(value):
    integer_number=int(value)
    return integer_number

# result = str_to_int("95556")
# print(result[3])

def division(val1,val2):
    try:
        result=val1/val2
        return result
    except ZeroDivisionError as e:
        print(f"Error, Details: {e}")
    except ValueError as e:
        print(f"Not Integer: Details: {e}")
    except TypeError as e:
        print(f"Wrong Type, Details: {e}")
    except Exception as e:
        print(f"Unknown Error, Details: {e}")
    finally:
        print("This Block will run always")
    

# result=division(1,3)
# if result==None:
#     result="No result returned from the function"
# print(result)

def validate_email(email):
    try:
        if "@gmail.com" not in email:
            raise ValueError("invalid gmail format")
        return {"Success":True, "email":email}
    except ValueError as e:
        return{"valid":False, "error":str(e)}

result=validate_email("amjadkhanniazi010@gmail.com")
print(result)