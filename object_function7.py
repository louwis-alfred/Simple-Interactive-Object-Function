# Parent / Based
class Car:
    # Assignment
    AnswerA = ""
    AnswerB = ""
    
    # Object Function
    def __init__(self,type,color,price,plateNumber):
        self.type = type
        self.color = color
        self.price = price
        self.plateNumber = plateNumber
        print(f"You selected a {self.type}")
        
        print(f"Here's the information:")
        
    def x (self):
        print(f"You have now {self.type}")
        
    def details (self):
        print(f'Type: {self.type}')
        print(f'Color: {self.color}')
        print(f'Price: {self.price}')
        print(f"Car number: {self.plateNumber}")
# User Input        
type = input('Enter Type: ').strip().capitalize()
color = input('Enter Color: ').strip().capitalize()
price = float(input('Enter price: '))
plateNumber = input('Enter car number: ').upper().strip()

carOne = Car(type,color,price,plateNumber)
carOne.details()
AnswerA = input('Do you want to buy this? ').strip().lower()

# Function
while True:
    if AnswerA == 'yes':
        print(f"You just bought a {type} with a price of {price}.")
        break
    elif AnswerA == 'no':
        break
    else:
        print(f"{AnswerA} is not on option")
# User Input       
while True:
    AnswerB = input('Do you want to continue? ').lower().strip()
    if AnswerB == 'yes':
        type = input('Enter type: ').strip().capitalize()
        color = input('Enter color: ').capitalize().strip()
        price = float(input('Enter price: '))
        plateNumber = input('Enter plate number: ').upper().strip()
        carTwo = Car(type,color,price,plateNumber)
        carTwo.details()
        
    elif AnswerB == 'no':
        print('See you next time, Thanks for comming!')
        break
        
        
