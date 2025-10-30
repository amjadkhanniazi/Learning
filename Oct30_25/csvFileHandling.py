import csv
import os
def save_csv(userdata, filename="users.csv"):
    try:
        file_exists = os.path.isfile(filename)
        with open(filename, 'a', newline="") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=["name", "age", "email"])
            if not file_exists:
                writer.writeheader()
            for user in userdata:
                writer.writerow(user)
            return True
    except IOError:
        return False

def load_csv(filename="users.csv"):
    users=[]
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                users.append(row)
        return users
    except FileNotFoundError:
        return []


# var = save_csv([{"name": "Alice", "age": 23, "email": "domael"}, {"name": "Bob", "age": 30, "email": "Bob@gmail.com"}])


var2 = load_csv()
print(var2)