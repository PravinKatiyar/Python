
'''
NOTE: To make mysql connector to work in system install mysql-connector.
pip install mysql-connector-python
'''
import mysql.connector as connector
from Employee import Employee

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='toor',
                                     database='javaspring') #database/schema name
        query = 'CREATE TABLE IF NOT EXISTS Employee (ID int NOT NULL AUTO_INCREMENT, Name varchar(255) NOT NULL, DeptName varchar(' \
                '255),Age int,PRIMARY KEY (ID)) '
        cur = self.con.cursor()
        cur.execute(query)
        print("Table Created!!")


# -----------------Create Employee---------------------------
    def create_employee(self,  employee):
      #  empId=employee.get_empId()
        name=employee.get_name()
        deptName=employee.get_deptName()
        age=employee.get_age()
        query = "insert into Employee(Name,DeptName,Age) values('{}','{}',{})".format(name, deptName, age)
       # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Employee saved successfully!!")


# -----------------Fetch All Employees-----------------------
    def fetch_all_employees(self):
        employee_list = []
        query="select * from Employee"
        cur=self.con.cursor()
        cur.execute(query)
        #emp=Employee
        print("-----------------------------------")
        for row in cur:
            empid=row[0]
            empName = row[1]
            empDept = row[2]
            empAge = row[3]
            emp=Employee(empid,empName,empDept,empAge)
            employee_list.append(emp)
        return employee_list
# -----------------Delete Employee by Id---------------------
    def delete_user(self,empId):
        cur = self.con.cursor()
        cur.execute("select id from Employee where id={}".format(empId))
        data = cur.fetchall()
        if (len(data) == 0):
            print("Employee with Id {} not found!".format(empId))
        else:
            query = "delete from Employee where ID={}".format(empId)
            cur.execute(query)
            self.con.commit()
            print("Employee deleted successfully!!")

# -----------------Fetch Employee by Id---------------------
    def select_user_byId(self, empId):
        cur = self.con.cursor()
        cur.execute("select id from Employee where id={}".format(empId))
        data = cur.fetchall()
        if (len(data) != 0):
            query = "select * from Employee where ID={}".format(empId)
            cur.execute(query)
            myresult = cur.fetchone()
            emp = Employee(myresult[0], myresult[1], myresult[2], myresult[3])
            return emp
        else:
            return None


    # -----------------Update Employee by Id---------------------
    def update_employee(self, employee):
        existingEmpId = employee.get_empId()
        updated_name = employee.get_name()
        updated_deptName = employee.get_deptName()
        updated_age = employee.get_age()
        cur = self.con.cursor()
        cur.execute("select id from Employee where id={}".format(existingEmpId))
        data = cur.fetchall()
        if (len(data)==0):
            print("Employee with Id {} not found!".format(existingEmpId))
        else:
            query = "update Employee set Name='{}',DeptName='{}',Age={} where ID={} ".format(updated_name, updated_deptName, updated_age, existingEmpId)
            cur.execute(query)
            self.con.commit()
            print("Employee updated successfully!!")

helper = DBHelper()
#helper.create_employee(42, "Pravin", "FS", 24)
#helper.delete_user(42)
#helper.fetch_all_employees()
#helper.select_user_byId(47)
#helper.update_employee(47,'Pravin','CSD',25)