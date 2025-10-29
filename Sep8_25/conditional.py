height=4.2
if height>=6:
    status="Tall"
elif height<6 and height>5:
    status="Average"
elif height<5:
    status="Short"

print(f"The person is {status}")