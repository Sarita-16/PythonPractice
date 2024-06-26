class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age         # private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        flag = 0
        if age >= 18:
            self.__age = age
        else:
            flag = 1
            print("You are nor an Adult :]")
            return flag

p = person("Sarita", 23)
print(f"Name : {p.name}")
print(f"Age : {p.get_age()}")
result = p.set_age(10)
if result == 1:
    pass
else:
    print(f"After changing Age : {p.get_age()}")