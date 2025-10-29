def add(a,b):
    return a+b

# print(add(2,4))


add_lambda=lambda x,y,z: x+y+z
# print(add_lambda(1,5,2))

square=lambda x:x**2

ans=square(4)
# print(ans)

is_even=lambda x:x%2==0
# print(is_even(6))
# print(is_even(7))

upper=lambda word: word.upper()
print(upper("amjad"))