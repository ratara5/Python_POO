class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    
    def description(self):
        print('Name: {}\nAge: {}\nAddress: {}'.format(self.name,self.age,self.address))

class Employee(Person):
    def __init__(self, employee_name,employee_age, employee_address, salary, seniority):
        super().__init__(employee_name,employee_age,employee_address)
        self.salary=salary
        self.seniority=seniority
    
    def description(self):
        super().description()
        print('Salary: {}\nSeniority: {}'.format(self.salary,self.seniority))

p1=Person('Antoine',50,'Happycity')
p1.description()


print('\n----------Now. I create an object of the Employee class what is subclass of Person----------')
e1=Employee('Frederich',35,'Berlin',20000,5)
e1.description()

print(isinstance(e1,Employee)) #Every object of the class Employee is Employee
print(isinstance(e1,Person)) #Every object of the class Employee is Person
print(isinstance(p1,Employee)) #Not every object of the class Employee is Person