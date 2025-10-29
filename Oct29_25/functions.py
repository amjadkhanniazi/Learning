class adminUser():
    def __init__(self, username, email, permissions=None):
        
        self.username = username
        self.email = email
        if permissions is None:
            self.permissions = []
        else:
            self.permissions = permissions
    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)
    def can_access(self, resource):
        return resource in self.permissions or "admin" in self.permissions
    
admin = adminUser("admin_bob", "bob@gmail.com", ["admin"])
print(admin.can_access("Hello"))