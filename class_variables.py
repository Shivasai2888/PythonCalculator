
class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Shiva", 21)
student2 = Student("Ravi", 20)
student3 = Student("Aradhan", 20)

print(student1.name)
print(student2.age)
print(student1.age)
print(student2.name)
print(student3.name)
print(student3.class_year)

print(f"your name is {student1.name}  age  {student1.age}  year {student1.class_year} No of students{Student.num_students}")


print(Student.num_students)
