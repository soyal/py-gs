# coding=UTF-8


class Robot:
  '''机器人'''
  # 类变量，相当于静态变量
  population = 0

  def __init__(self, name):
    '''初始化数据'''
    self.name = name
    print('init robot name:{}'.format(name))
    Robot.population += 1

  def sayHi(self):
    print("Greeting, my master call me {}".format(self.name))

  def selfHowMany(self):
    # 实例可以通过__class__访问它的类
    print('the robot know how many robots there are: ', self.__class__.population)

  # 类方法
  # classmethod与staticmethod的区别在于 classmethod会将类作为第一个参数传入，staticmethod不会
  @classmethod
  def howMany(cls):
    '''打印当前的人口数量'''
    print('we have {:2d} robots'.format(cls.population))

print(Robot.__doc__)
robot = Robot('x')
robot.sayHi()
Robot.howMany()

robot2 = Robot('xx')
robot2.sayHi()
Robot.howMany()
robot2.selfHowMany()
