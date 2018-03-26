# coding=UTF-8

# 继承


class SchoolMember:
  '''学校成员'''

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def tell(self):
    '''告知细节'''
    print('name: {name}, age: {age}'.format(name=self.name, age=self.age), end = ', ')

class Teacher(SchoolMember):
  '''老师'''
  def __init__(self, name, age, salary):
    SchoolMember.__init__(self, name, age)
    self.salary = salary
  def tell(self):
    SchoolMember.tell(self)
    print('Salary: {:d}'.format(self.salary))

class Student(SchoolMember):
  '''学生'''
  def __init__(self, name, age, marks):
    SchoolMember.__init__(self, name, age)
    self.marks = marks
  def tell(self):
    SchoolMember.tell(self)
    print('Marks: {:d}'.format(self.marks))

if __name__ == '__main__':
  teacher = Teacher('alice', 23, 4000)
  student = Student('eric', 16, 100)

  teacher.tell()
  student.tell()