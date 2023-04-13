##oop
#1
class people():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greets(self):
        print("hello",self.name)
p1=people(name="gill", age=23)
p1.greets()
print(p1.name)
#2
class student():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print("hello this is",self.name,"age",self.age,"gender",self.gender)
s1=student(name="gill", age=23, gender="M")
s1.info()
#3
class student():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print("Name of student:",self.name)
    def report(self,score):
        print("Score",str(score))
s1=student(name="gill",age=23,gender="M")
s1.info()
s1.report(66)
#4
class Sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}
    def add_data(self, t, data):
        self.data['time'] = t
        self.data['data'] = data
        print(f'We have {len(data)} points saved')         
    def clear_data(self):
        self.data = {}
        print('Data cleared!')
class NewSensor(Sensor):
    def __init__(self, name, location, record_date, brand):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.brand = brand
        self.data = {}  
new_sensor = NewSensor('OK', 'SF', '2019-03-01', 'XYZ')
new_sensor.brand
##problems
#1
import matplotlib.pyplot as plt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def plot_point(self):
        plt.scatter(self.x, self.y)
        plt.show()
p = Point(1, 2)
p.plot_point()
#2


