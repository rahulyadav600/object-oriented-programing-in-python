# A class method is bound to the class & receives the class as an implicit first argument
#  note - static method cannot access or modify class state & generally for utility
class Person:
    name = "anonymous"   # ✅ class variable

    @classmethod
    def changeName(cls, name):   # ✅ class method
        cls.name = name


# Create object
p1 = Person()

# Call class method using object
p1.changeName("rahul kumar")

# Print results
print(p1.name)     # rahul kumar
print(Person.name) # rahul kumar
