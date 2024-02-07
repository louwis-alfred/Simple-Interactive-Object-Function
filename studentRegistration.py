class Student:
    def __init__(self,name,course,year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section
        
    def reg(self):
        print(f'Name: {self.name}')
        print(f'Course: {self.course}')
        print(f'Year: {self.year}')
        print(f'Section: {self.section}')
        print()
   
listofStudent = []    
 
while True:
    # User input
    name = input('Name: ').strip().title()
    course = input('Course: ').strip().title()
    year = input('Year: ')
    section = input('Section: ').strip().title()
    s = Student(name,course,year,section)
    listofStudent.append(s)
    print()
    choice = input('Create another student? [Y / N] : ').lower()
    if choice == 'y': pass
    elif choice == 'n':
        break
    else:
        print(f'{choice} is not in option')

# Itiration of Students
i = 0
print('Registered Students:')
for student in listofStudent:
    i += 1
    print('Student #',str(i))
    student.introduce()