class Student:
    def student_action(self):
        print("I am pursuing Master's Degree")

class Teacher:
    def teacher_action(self):
        print("I Teach computer science")


class Youtuber:
    def youtuber_action(self):
        print("I make videos to play guitar")

class Person(Teacher,Student,Youtuber):
    pass

Aarohi = Person()
Aarohi.student_action()
Aarohi.teacher_action()
Aarohi.youtuber_action()