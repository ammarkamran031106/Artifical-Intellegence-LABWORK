#You are designing a University Staff Management System. The system needs to keep
#track of different staff members: Teachers, Administrative Staff, and Research
#Assistants. All staff share common attributes like name, staff_id, and department, but
#each type has its own specific properties and behaviors. Teachers have courses and
#salary and can teach courses, Admin Staff have role and working_hours and perform
#tasks, while Research Assistants have research_topic and stipend and work on research.
#Your task is to create a base class Staff and derive classes for each staff type, instantiate
#objects, and call their respective methods to simulate daily activities. Optionally,
#override the display_info() method to show type-specific details.
# Parent class
class Staff:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.department)


# Teacher class
class Teacher(Staff):
    def __init__(self, name, id, department, course, salary):
        super().__init__(name, id, department)
        self.course = course
        self.salary = salary

    def teach(self):
        print("Teaching course:", self.course)

    def display(self):   # overridden method
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.department)
        print("Course:", self.course)
        print("Salary:", self.salary)

# Administrator class
class Administrator(Staff):
    def __init__(self, name, id, department, w_hours):
        super().__init__(name, id, department)
        self.w_hours = w_hours

    def roles(self, option):
        if option == 1:
            print("FEES COLLECTION")
        elif option == 2:
            print("ATTENDANCE")
        elif option == 3:
            print("ADMISSIONS")
        elif option == 4:
            print("FINANCE")
        else:
            print("EXIT")

    def display(self):   # overridden method
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.department)
        print("Working Hours:", self.w_hours)



# Research Assistant class
class Research_Assistant(Staff):
    def __init__(self, name, id, department, topic, budget):
        super().__init__(name, id, department)
        self.topic = topic
        self.budget = budget

    def work(self):
        print("Researching in progress on:", self.topic)

    def display(self):   # overridden method
        print("Name:", self.name)
        print("ID:", self.id)
        print("Department:", self.department)
        print("Research Topic:", self.topic)
        print("Budget:", self.budget)




# Create objects
t1 = Teacher("Ali", 101, "CS", "Python", 80000)
a1 = Administrator("Sara", 201, "Admin", 8)
r1 = Research_Assistant("Ahmed", 301, "Biotech", "Cancer Research", 500000)

# Teacher activities
print("\n--- Teacher ---")
t1.display()
t1.teach()

# Administrator activities
print("\n--- Administrator ---")
a1.display()
a1.roles(1)
a1.roles(3)

# Research Assistant activities
print("\n--- Research Assistant ---")
r1.display()
r1.work()
