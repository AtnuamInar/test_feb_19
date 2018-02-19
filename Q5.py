#!/usr/bin/python3
class Student:
    def __init__(self, name, section):
         self.name = name
         self.sec = section
 
 
    @classmethod
    def gen_stu_from_string(cls, inp):
        name, sec = inp.split("-")
        return cls(name, sec)
     
stu1 = Student.gen_stu_from_string("maunta-b")
 
print(stu1.__dict__)
