#Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    
    def display(self):
        print(f"ID: {self.id}\n Name={self.name}")
        
emp=Employee(1,'coder')
emp.display()

#use del propery to first delete id attribute and then the entire object
del emp.id
#deleting the object
del emp

try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()
    #it will gives error after deleting emp
except NameError:
    print("emp is not defined")