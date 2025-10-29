class animal:
    def __init__(self, name, species, age):
        self._name=name
        self._species=species
        self._age=age
    @property
    def details(self):
        return {"name": self._name, "species":self._species,"age":self._age}

    @details.setter
    def details(self, details_dict):
        self._name=details_dict["name"]
        self._species=details_dict["species"]
        self._age=details_dict["age"]
    def movement(legs):
        if legs==2:
            return 

    

ani1=animal("dog","mammal", 12)

print(ani1.details)
ani1.details={"name":"zebra","species":"mammal","age":22}
print(ani1.details)
