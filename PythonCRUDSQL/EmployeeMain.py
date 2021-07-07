from PythonCRUDSQL.python_db_con import DBHelper
from PythonCRUDSQL.Employee import Employee
def main():
    dBhelper=DBHelper()
    while True:
        print("--------------MENU-----------------")
        print()
        print("Press 1 to Create Employee")
        print("Press 2 to Fetch All Employees")
        print("Press 3 to Fetch Employee by Id")
        print("Press 4 to Update Employee by Id")
        print("Press 5 to Delete Employee by Id")
        print("Press 6 to Exit")

        print()
        try:
            choice=int(input())
            if(choice==1):
                #Create Employee
                emp_id =None
                emp_name =str(input("Enter employee Name: "))
                emp_deptName =str(input("Enter employee Dept Name: "))
                emp_age =int(input("Enter employee Age: "))
                employee=Employee(emp_id, emp_name,emp_deptName,emp_age)
                dBhelper.create_employee(employee)

            elif choice==2:
                #Fetch All Employees
                employee_list = dBhelper.fetch_all_employees()
                for employee in employee_list:
                    print("Employee Id       : {}".format(employee.get_empId()))
                    print("Employee Name     : {}".format(employee.get_name()))
                    print("Employee Dept Name: {}".format(employee.get_deptName()))
                    print("Employee Age      : {}".format(employee.get_age()))
                    print("-----------------------------------")

            elif choice == 3:
                #Fetch Employee by Id
                emp_id =int(input("Enter employee Id: "))
                emp =dBhelper.select_user_byId(emp_id)
                if(emp is None):
                    print("Employee with Id {} not found!".format(emp_id))
                else:
                    print("Employee Id       : {}".format(emp.get_empId()))
                    print("Employee Name     : {}".format(emp.get_name()))
                    print("Employee Dept Name: {}".format(emp.get_deptName()))
                    print("Employee Age      : {}".format(emp.get_age()))


            elif choice == 4:
                #Update Employee by Id
                emp_id = int(input("Enter employee Id: "))
                emp_name = str(input("Enter employee Name: "))
                emp_deptName = str(input("Enter employee Dept Name: "))
                emp_age = int(input("Enter employee Age: "))
                employee1 = Employee(emp_id, emp_name, emp_deptName, emp_age)
                dBhelper.update_employee(employee1)

            elif choice == 5:
                #Delete Employee by Id
                emp_id = int(input("Enter employee Id: "))
                dBhelper.delete_user(emp_id)

            elif choice == 6:
                #Exit
                break
            else:
                print("Invalid input!! Try Again")
        except Exception as e:
            print(e)
            print("Invalid Details !!")

if __name__=="__main__":
    main()