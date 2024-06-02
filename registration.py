class Person:
    name_of_registered_accounts = []
    how_many_registered_accounts = 0
    
    def __init__(self, firstname: str, lastname: str, age: int, gender: str):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        Person.how_many_registered_accounts += 1
        Person.name_of_registered_accounts.append(f"{self.firstname} {self.lastname}")
        print('Registered successfully')
        
    def introduce(self):
        print(f'Hello, {self.firstname}!')

while True:
    firstname = input("Enter your firstname: ").capitalize()
    lastname = input("Enter your lastname: ").capitalize()
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ").capitalize()
    
    person = Person(firstname, lastname, age, gender)
    person.introduce()
    
    cont = input("Do you want to continue? [Yes/No]: ").strip().lower()
    if cont != "yes":
        break
    
print()
print(f"Total number of registered accounts: {Person.how_many_registered_accounts}")
print(f"Names of registered accounts:")
for i, name in enumerate(Person.name_of_registered_accounts, start=1):
    print(f"{i}. {name}")
