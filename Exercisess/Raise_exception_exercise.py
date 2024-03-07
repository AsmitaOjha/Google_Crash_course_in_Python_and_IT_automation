#for making exception just make subclass of Exception
class AdultException(Exception):
    pass




#Create a class Person with attributes name and age in it.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.
    def get_minor_age(self):
        if self.age<=18:
            return self.age
        else:
            raise AdultException
        
    def display_person(self):
        try:
            print(f"age= {self.get_minor_age()}")
        except AdultException:
            print("Person is adult.......")
        finally:
            print(f"name={self.name}")
        
Person("Aarohi",17).display_person()
Person("Rashmi",19).display_person()
