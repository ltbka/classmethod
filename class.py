# # агрегация слабая связь
# # композиция сильная связь


# class Engine:
#     value = 2.3

# class Wheel:
#     size = 15

# class Korobka:
#     tipe = 'avtomat'


# class Car:
#     def __init__(self, korobka) -> None:
#         self.korobka = korobka           #  ---  Композиция
#         self.engine = Engine()           #  ---  Агрегация
#         self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]

# korobka = Korobka()
# car = Car(korobka)

# # print(car.engine.value)
# # print(car.wheels[0].size)

# #================= Композиция 

# class Salary:
#     def __init__(self, pay) -> None:
#         self.pay = pay

#     def get_total(self):
#         return (self.pay * 12)
    

# class Employee:
#     def __init__(self, pay, bonus) -> None:
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)

#     def full_salary(self):
#         return f'Total {self.salary.get_total() + self.bonus} '
    
# # employee = Employee(1000, 20)
# # print(employee.full_salary())



# class Salary:
#     def __init__(self, pay) -> None:
#         self.pay = pay

#     def get_total(self):
#         return (self.pay * 12)
    

# class Employee:
#     def __init__(self, pay, bonus) -> None:
#         self.pay = pay
#         self.bonus = bonus

#     def full_salary(self):
#         return f'Total {self.pay.get_total() + self.bonus}'

# salary = Salary(200)
# # employee = Employee(salary, 15)
# # print(employee.full_salary())



# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100


# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.batter = Battery()

# class Samsung:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery
    

# iphone = Iphone('black')

# battery = Battery()
# samsung = Samsung(battery, 'white')



# # =================== Методы в ооп 


# # Методы экземпляра 

# # Методы класса

# # Статические методы 


# # class A:
# #     def instance_method(self):
# #         # print('Метод обьекта')
# #         # print('Первый аргумент ', self)

# # obj_a = A()
# # obj_a.instance_method()


# # Методы класса нужны для создания обьектов и измененя атрибутов класса 
# # Для того чтобы сделать метод методом класса нужно обернуть в декоратор

# # class B:
# #     @classmethod
# #     def class_method(cls):
#         # print('Класс Метод')
#         # print('Первый аргумент: ', cls)

# # obj_b = B()
# # obj_b.class_method()



# # class Car:
# #     color = 'blue'

# #     @classmethod
# #     def change_color(cls, value):
# #         print(cls)
# #         cls.color = value

# #     def change_color(self, value):
# #         print(self)
# #         self.color = value

# # mers = Car()
# # tayota = Car()

# # print(mers.color)
# # print(tayota.color)
# # mers.change_color('vailet')
# # print(mers.color)
# # tayota.change_color('yellow')
# # print(tayota.color)
# # Car.change_color('orenge')
# # print(mers.color)
# # print(tayota.color)



# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()

#     def __del__(self):
#         self._dec_counter()
#         del self
    
#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1

#     @classmethod
#     def _dec_counter(cls):
#         cls.counter -= 1

# # obj1 = C()
# # obj2 = C()
# # obj3 = C()
# # del obj2
# # print(C.counter)


# # class Pizza:
# #     def __init__(self, raidus, ingredients) -> None:
# #         self.radius = raidus
# #         self.ingredients = ingredients
        
# #     def cook(self):
        
        
# #     @classmethod
# #     def four_cheese(cls, r):
# #         pizza2 = cls(18, 'моцарела','пармизан','голандский','чеддер')
# #         return Pizza

# # pizza1 = Pizza(15, 'пеперони','моцарела','ананас')
# # # pizza2 = Pizza(18, 'моцарела','пармизан','голандский','чеддер')
# # pizza2 = Pizza.four_cheese(15)
# # pizza3 = Pizza.four_cheese(20)

# # pizzas = [pizza1, pizza2, pizza3]

# # for pizza in pizzas:
# #     pizza.cook()

# #pow вoзводит в степень
# #Не принимает ни обьект ни класс
# #такие методы полезны для создания вспомогательных функция или расчетов
# #статические методы не имеют доступ к атрибутам и методам обьекта и класса

# # class B:
# #     @staticmethod
# #     def pow_x(x):
# #         print( x ** 2)
        
# # b = B()
# # b.pow_x(2)

# class A:
    
    
#     def __init__(self, name) -> None:
#         self.name = name
        
#     @classmethod
#     def from_list(cls, lst):
#         return cls(lst)
    
# # a = A('mariiam')
# # b = a.from_list('mariiam2')
# # print(b)
# # print(id(a))
# # print(id(b))


# import os


# # class Iphone13:
# #     cost = 70000
# #     def __init__(self, name, money) -> None:
# #         if money < Iphone13.cost:
# #             raise Exception('Вам не хватило денег на покупку нового айфона')
# #         self.name = name
        
# #     @staticmethod
# #     def about_phone():
# #         print('Good new phone')
        
        
# #     @classmethod
# #     def change_cost(cls, new_cost):
# #         cls.cost = new_cost
        
# #     @staticmethod
# #     def info_dir():
# #         print(os.system('ls -la'))
# #         print(os.system('mkdir new_dir'))

# # atai = Iphone13('atai', 80000)
# # atai.info_dir()
# # atai.change_cost(50000)
# # rakhim = Iphone13



# # class MathUtils:
# #     @staticmethod
# #     def multiply(a, b):
# #         return a * b

# # # result = MathUtils.multiply(2, 3)
# # # print(result)
        



