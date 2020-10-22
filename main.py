# Import classes from class.py file
from class import Employee, Temporary, Permanent
# Create an Employee   

john=Temporary('John Wall', '19/06/1975', 'E0001')
john.hourlyrate = float(5.55)
john.weeklyhours = float(37.5)

stuart=Permanent('Stuart Riding', '06/06/1975', 'E0002')
stuart.annualsalary = 36000
stuart.pensionplan = "Member"

mike=Permanent('Micheal Myers', '07/05/1971', 'E0003')
mike.annualsalary = 43000
mike.pensionplan = "Member"

#Program to access the data

active = True

while active == True:
    print("\n")
    print("Please choose from the following options: ")
    print("\n")
    print("1. Class Details")
    print("2. Employee Numbers")
    print("3. Employee Details")
    print("\n")
    command = input("> ")
    #Check the command entered
    if command == "1": # Print the Class Details.  Display the output of the __str__ methods for each sub-class
        print(stuart)
        print(john)
    elif command == "2": # Print the Employee Numbers
        all = int(Temporary.number_of_temp_emp) + int(Permanent.number_of_perm_emp)
        print(f"Total number of Temporary Employees: {Temporary.number_of_temp_emp}")
        print(f"Total number of Permanent Employees: {Permanent.number_of_perm_emp}")
        print(f"Total number of Employees: {all}")        
    elif command == "3": #Enter a second loop to access Employee Details
        print("\n")
        print("Select your Employee:") # Select which Employee details you wish to see
        print("1. John Wall")
        print("2. Stuart Riding")
        print("3. Michael Myers")
        selection = input("> ")
        if selection == "1":
            john.display() # Display the Employee's Personal Data.  Method from the Parent Class
            john.salary_info() # Display the Employee's Salary datat.  Method fromt he Sub Classe 
        elif selection == "2":
            stuart.display()  # Display the Employee's Personal Data.  Method from the Parent Class
            stuart.salary_info() # Display the Employee's Salary datat.  Method from the Sub Class 
        elif selection == "3":
            mike.display()  # Display the Employee's Personal Data.  Method from the Parent Class
            mike.salary_info() # Display the Employee's Salary datat.  Method from the Sub Class 
        else:
            print("Invalid ID.  Please try again.") # Invalid Employee entered.  Start Again
    else:
        active = False  # Press any other button, and the programme ends

