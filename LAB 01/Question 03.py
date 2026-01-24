#INPUT NAME AND MARKS OF STUDENTS AND STORE THEM IN DICTIONARY AND THEN PRINT THEM
name1=(input("Enter A Name:"))
marks1=(input("Enter A Marks:"))
name2=(input("Enter A Name :"))
marks2=(input("Enter A Marks:"))
name3=(input("Enter A Name :"))
marks3=(input("Enter A Marks:"))
students={name1:marks1,name2:marks2,name3:marks3}

print('Student Records:')
for name, marks in students.items():
    print(name, ":", marks)
