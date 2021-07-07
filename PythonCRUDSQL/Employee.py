
class Employee:
  def __init__(self, empId, name,deptName,age):
    self.empId = empId
    self.name = name
    self.deptName = deptName
    self.age = age

  def __str__(self):
    return "{} {} {} {}".format(self.empId,self.name,self.deptName,self.age)

#-----getter---------
  def get_empId(self):
    return self.empId

  def get_name(self):
    return self.name

  def get_deptName(self):
    return self.deptName

  def get_age(self):
    return self.age

#-------setter-----------
  def set_empId(self, empId):
    self.empId=empId

  def set_name(self, name):
    self.name=name

  def set_deptName(self, deptName):
    self.deptName=deptName

  def set_age(self, age):
    self.age=age
