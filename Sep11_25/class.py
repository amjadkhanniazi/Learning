class User:
    """User class for Web Application"""
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
        self.login_count = 0
    def login(self):
        """Similate user login"""
        self.login_count +=1
        return f"User {self.username} Logged In. Total Logins: {self.login_count}"
    def deactivate(self):
        self.is_active=False
    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}')"
    
#Usage
user = User("amjad123","amjad@gmail.com")
user2 = User("amjad12","amjad1@gmail.com")
# print(user.login())
#print(user2)

class BankAccount:
    def __init__(self, balance):
        self.balance=balance
        self.transactions=[]
    def deposit(self, Amount):
        self.balance +=Amount
        self.transactions.append(f"Deposited: {Amount}")
        self._log_transaction()
    def _log_transaction(self):
        print(f"Account Balance: {self.balance}")

account1 = BankAccount(100)
account2= BankAccount(200)

# account1.deposit(50)
# account1.deposit(100)
# print(account1.balance)

class AdminUser(User):
    def __init__(self, username, email, permissions=None):
        super().__init__(username, email)
        self.permissions=permissions or []
    def add_permissions(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)
    def can_access(self,resource):
        return resource in self.permissions or "admin" in self.permissions
    
# Usage
admin = AdminUser("admin_bob", "bob@company.com",["admin"])
print(admin.can_access("user_management"))