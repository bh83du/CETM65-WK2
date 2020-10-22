'''
Create a Employee Class

'''
class Employee():

# Define the details for the Employee class
    def __init__(self, name,dob,emp_id):
        self.name = name
        self.dob = dob
        self.id = emp_id


# Add a __str__ method to give a Human readable desciption of the class. 
    def __str__(self):
        return "This is the Employee Class __str__"

# Add a __repr__ method to return the Class used to create the object
    def __repr__(self):    
        return "Employee(self, name,dob,emp_id)"

# Method to display the Employee's information

    def display(self):
        print('\n') # Inserts new line.
        print("The Employee's name is: " + self.name)
        print("The Employee's date of Birth is " + self.dob)
        print("The Employee's ID is " + self.id)
        print("\n")

'''
Create a Sub Class of Employee for Temporary Employees
'''
# Need to add Decoraters and Properties tags.  Must be clearner way to do it.
class Temporary(Employee):

    number_of_temp_emp = 0  # Class variable to allow tracking of number of Employees

    def __init__(self, name, dob, emp_id):
        super().__init__(name, dob, emp_id) # Attributes inherited from Employee Class
        self.hourlyrate = None              # Hourly Rate specific to Temporary Class
        self.weeklyhours = None             # Weekly Hours specific to Temporary Class
        self.tgp = None                     # Temporary Gross Weekly Pay
        Temporary.number_of_temp_emp = Temporary.number_of_temp_emp + 1  # Add to running total of Temporary Employees

# Add a __str__ method to give a Human readable desciption of the class. 

    def __str__(self):
        return "This is the Temporary Employee Class __str__method"

# Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Temporary(self, name,dob,emp_id)"

# Method to calculate the gross weekly wage of the Employee

    def salary_info(self):
        self.tgp = (self.hourlyrate * self.weeklyhours)
        print('\n')
        print(f'Contract Type is Temporary')
        print(f'Employee hourly rate is: £{self.hourlyrate}')
        print(f'Employee contracted weekly hours are: {self.weeklyhours} hours')
        print(f'Employee gross weekly salary is: £{self.tgp}')

        

'''
Create a Sub Class of Employee for Permanent Employees
'''
# Need to add Decoraters and Properties tags.  Must be clearner way to do it.
class Permanent(Employee):

    number_of_perm_emp = 0 # Class variable to allow tracking of number of Employees


    def __init__(self, name, dob, emp_id, ):
        super().__init__(name, dob, emp_id) # Attributes inherited from Employee Class
        self.annualsalary = None            # Annual Salary specific to Permanent Class
        self.pensionplan = None             # Pension Plan Status for Permanent Class
        self.pgp = None                     # Permanent Gross Weekly Pay
        # Increment the number of permanent employees by 1
        Permanent.number_of_perm_emp = Permanent.number_of_perm_emp + 1

# Add a __str__ method to give a Human readable desciption of the class. 

    def __str__(self):
        return "This is the Permanent Employee Class __str__ method"

# Add a __repr__ method to return the Class used to create the object

    def __repr__(self):
        return "Permanent(self, name,dob,emp_id)"

# Add a method to calculate the Permanent Gross Weekly salary
    def salary_info(self):
        self.pgp = (self.annualsalary / 52)
        print('\n')
        print(f'Contract Type is Permanent')
        print(f'Employee Annual Salary is: £{self.annualsalary}')
        print(f'Employee Pension Scheme Status: {self.pensionplan}')
        print(f'Employee gross weekly salary is: £{self.pgp}')

# End of the file - Just an update for a Commit