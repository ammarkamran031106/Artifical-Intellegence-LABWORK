class Employee:
  
  def __init__(self, name, emp_id ):
        self.name= name
        self.emp_id = emp_id




class FullTImeEmployee(Employee):
  def __init__(self, name, emp_id, salary):
    super().__init__(name, emp_id)
    self.salary = salary

  def cal_salary(self):
    return self.salary






class PartTimeEmployee(Employee):
  def __init__(self, name, emp_id, hours_worked):
    super().__init__(name, emp_id)
    self.hours_worked = hours_worked

  def cal_salary(self,hours,hours_rate):
    return self.hours_worked*hours_rate



#Create object
employee1=FullTImeEmployee("Ammar", 3423, 500000)
salary1=employee1.cal_salary()
print("FULL TIME EMPLOYEE SALARY : ",salary1)
print()


employee2=PartTimeEmployee ( "Amman" , 4567, 6)
hours_worked=int(input("Enter the hours worked : "))
salary2=employee2.cal_salary(hours_worked,3000)
print()
print("PART TIME EMPLOYEE SALARY per HOUR : ",3000)
print("PART TIME EMPLOYEE SALARY ON WORKING ", hours_worked ,"IS : ", salary2)

  
