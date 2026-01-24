#Write a Python function named calculate_average() that takes a list of marks and returns the
#average marks.
def calculate_average(marks):
    total = 0
    for i in range(len(marks)):
        total = total + marks[i]
    average = total / len(marks)
    return average


marks = []

marks1=int(input("Enter mark 1: "))
marks2=int(input("Enter mark 2: "))
marks3=int(input("Enter mark 3: "))

marks =[marks1,marks2,marks3]
avg = calculate_average(marks)
print("Average Marks:", avg)
