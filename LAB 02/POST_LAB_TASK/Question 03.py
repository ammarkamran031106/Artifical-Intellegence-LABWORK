class Student:
  
  def __init__(self, name, marks ):
        self.name= name
        self.__marks= marks
  def set_marks(self, marks):
    self.__marks= marks



  def get_marks(self):
    return self.__marks

 
  
  def calculate_grade(self):
    if self.__marks >= 90:
      return "A"
    elif self.__marks >= 80:
      return "B"
    elif self.__marks >= 70:
      return "C"
    elif self.__marks >= 60:
      return "D"
    else:
      return "F"


#Create object
s1=Student("Ammar", 95)
s2=Student("Ali", 85)
s3=Student("Hamza",60)

s1.calculate_grade()
s2.calculate_grade()
s3.calculate_grade()

print("Student Name : ", s1.name)
print("Student Marks : ", s1.get_marks())
print("Student Grade : ", s1.calculate_grade())
print()

print("Student Name: ", s2.name)
print("Student Marks: ", s2.get_marks())
print("Student Grade: ", s2.calculate_grade())
print()

print("Student Name: ", s3.name)
print("Student Marks: ", s3.get_marks())
print("Student Grade: ", s3.calculate_grade())
print()

print("Student name: " ,s1.name)  #name is not private and not encapsulated with class so can be accessed directly
#print("Student marks: " ,s1.marks) #marks are private attribute encapsulated with class so cant access directly 
