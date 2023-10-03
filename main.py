# # print(len([1,2,3,4]))
# # print(len('123123'))
# # print(len({1:2, 3:4}))

# # # полеморфизм это возможность использовать одну  тот же  метод для обьектов от разных классов
# # # при этом результат меняется в зависимости к какому классу принадлежит обьект



# # def sum_elements(a, b):
# #     return a + b
# # print(sum_elements('a', 'b'))
# # print(sum_elements(1,2))




# # class Cat:
# #     def __init__(self, name, age) -> None:
# #         self.name = name
# #         self.age = age
        
# #     def make_sound(self):
# #         print('meeeooowwww')
        
# # class Dog:
# #     def __init__(self, name, age) -> None:
# #         self.name = name
# #         self.age = age
# #     def make_sound(self):
# #         print('gaaaav')
        
        
# # cat = Cat('Cat',  2)
# # dog = Dog('Dog', 5)

# # for sound in [cat, dog]:
# #     sound.make_sound()

# # class ShapeMixin:
#     #класс для описания формы
    
# #     def __init__(self, name) -> None:
# #         self.name = name 
    
# #     def area(self):
# #         pass
    
# #     def __str__(self) -> str:
# #         return self.name
    
# # class Circle(ShapeMixin):
# #     def __init__(self, name, radius) -> None:
# #         super().__init__(name)
# #         self.radius = radius
        
# #     def area(self):
# #         from math import pi
# #         return pi*self.radius**2
    
# #     def __str__(self) -> str:
# #         return f'{self.name} - {self.leght}'
    
# # class Square(ShapeMixin):
# #     def __init__(self, length) -> None:
# #         super().__init__('Square')
# #         self.length = length
        
    
# #     def area(self):
# #         return self.length **2
    
# #     def __str__(self) -> str:
# #         return f'{self.name} - {self.leght}'






# # class Tomato:
# #     def type(self):
# #         print('vegetable')
        
# #     def color(self):
# #         print('red')
    
# # class Apple:
# #     def type(self):
# #         print('fruit')
    
# #     def color(self):
# #         print('red')

# # def func(obj):
# #     obj.type()
# #     obj.color()
    
# # obj_tomato = Tomato()
# # obj_aplle = Apple()
# # func(obj_tomato)
# # func(obj_aplle)
        

# # class India:
# #     def capital(self):
# #         print('Deli')
        
# #     def langht(self):
# #         print('')
        
# # class USA:
# #     def capital(self):
# #         print('washington')
        
# #     def language(self):
# #         print('English')
        

# # Абстракция - это выделение основных, наиболее значимых характеристик обьекта и игнорирование
# # второстепенных
# # Он предостовляет общие атрибуты и методы для дочерних классов

# # from abc import ABC

# # class A(ABC):  #Обьявили абстрактный класс
# #     def method(self):
# #         print('Я обычный метод')
        
# #     @abstractmethod
# #     def method(self):
# #         print('Я абстрактный метод')
        
# #     @abstractmethod
# #     def method3(self): #Обычно не определаем логику
# #         pass    
    
# # class B(A):
# #     pass


# # a = A() #Нельзя создать обьект от класса в котором есть абстрактные методы

# # b = B
       
# from abc import ABC, abstractmethod

# class People(ABC):
    
#     @abstractmethod
#     def eat(self):
#         pass
#     @abstractmethod
#     def water(self):
#         pass
#     @abstractmethod
#     def sleep(self):
#         pass 
#     @abstractmethod
#     def breathe(self):
#         pass

# class Person(People):
#     def __init__(self, name) ->None:
#         self.name = name
        
#     def eat(self):
#         print('Я умею жрать')
         
#     def water(self):
#         print('Я умею пить')
        
#     def sleep(self):
#         print('Я умею спать')
        
#     def breathe(self):
#         print('Я умею дышать')
        
# # person = Person('Олег')
# # person.eat()
# from math import pi
    
   
# class Shape(ABC):
    
#     @abstractmethod
#     def calculate_area(self):
#         pass
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         self.radius = radius
        
#     def calculate_area(self):
#         from math import pi
#         return self.radius ** 2 * pi
    
#     def calculate_perimeter(self):
#         return self.radius * 2 * pi
    
# class Reactangle(Shape):
#     def __init__(self, width, height) -> None:
#         self.widht = width
#         self.height = height
        
#     def calculate_area(self):
#         return self.height * self.widht
    
#     def calculate_perimeter(self):
#         return (self.height + self.widht) * 2
    
# circle = Circle(5)
# rectangle = Reactangle(4, 6)

# # print('Площадь круга', circle.calculate_area())
# # print('Площадь круга', circle.calculate_perimeter())
# # print('Площадь прямоугольника', rectangle.calculate_area())
# # print('Площадь прямоугольника', rectangle.calculate_perimeter())    
        
            
# class PaymentSystem(ABC):
    
#     @abstractmethod
#     def make_payment(self, amout):
#         pass
#     @abstractmethod
#     def get_balance(self):
#         pass
    
# class CreditCard(PaymentSystem):
#     def __init__(self, card_number, expiry_date):
#         self.card_number = card_number
#         self.expiry_date = expiry_date
#         self.balance = 1000
        
#     def make_payment(self, ammout):
#         if self.balance >= ammout:
#             self.balance -= ammout
#             print(f'Платеж на сумму {ammout} выполнен.Остаток баланса {self.balance} сом')
#         else:
#             print('Недостаточно средтсв')
        
#     def get_balance(self):
#         return self.balance
    
# class PayPal(PaymentSystem):
#     def __init__(self, email, password) -> None:
#         self.email = email
#         self.password = password
#         self.balance = 2000
        
#     def make_payment(self, ammout):
#         if self.balance >= ammout:
#             self.balance -= ammout
#             print(f'Платеж на сумму {ammout} выполнен.Остаток баланса {self.balance} сом')
#         else:
#             print('Недостаточно средтсв на PayPal')
        
#     def get_balance(self):
#         return self.balance
    
# credit_card = CreditCard('1234-1234-1234-1234', '12/25')
# paypal = PayPal('test@gmail.com', '12345678')

# credit_card.make_payment(500)
# paypal.make_payment(700)

# # print(credit_card.get_balance())
# # print(paypal.get_balance())



# """
# 1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram.
# При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int.
# При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send,
# в WhatsApp он принимает только text и выдает строку “I am sending a text ...” и вместо … должен быть сам текст сообщения.
# В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. Если image True,
# то выдается сообщение “I am sending a text … with some image ”,
# если  False - сообщение “I am sending a text … without image”. 
# В Telegram метод send принимает voice message в виде строки и выдает сообщение “I am sending a voice message ...”.
# Создайте объекты от этих классов и вызовите метод send у всех объектов.
# """
# class WhatsApp:
#     def __init__(self, phone_number):
#         self.phone_number = int(phone_number)

#     def send(self, text):
#         return f"I am sending a text '{text}'."


# class SnapChat:
#     def __init__(self, phone_number):
#         self.phone_number = int(phone_number)

#     def send(self, image, text):
#         if image:
#             return f"I am sending a text '{text}' with some image."
#         else:
#             return f"I am sending a text '{text}' without image."


# class Telegram:
#     def __init__(self, phone_number, username):
#         self.phone_number = int(phone_number)
#         self.username = username

#     def send(self, voice_message):
#         return "I am sending a voice message '{}'.".format(voice_message)

# whatsapp = WhatsApp(123456789) 
# snapchat = SnapChat(987654321)
# telegram = Telegram(555555555, 'my_username')

# whatsapp_message = whatsapp.send('Hello, WhatsApp!')
# snapchat_message = snapchat.send(True, 'Hello, SnapChat!')
# telegram_message = telegram.send('Hello, Telegram voice message!')

# print(whatsapp_message)
# print(snapchat_message)
# print(telegram_message)




# """
# 2) Создайте два класса A и B. В обоих классах есть метод count. 
# В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count,
# а в классе B он подсчитывает количество согласных.
# Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
# """
# class A:
#     def count(self, word):
#         vowels = "aeiouAEIOU"
#         count = 0
#         for char in word:
#             if char in vowels:
#                 count += 1
#         return count


# class B:
#     def count(self, word):
#         consonants = 'jncjondcndoncondIJNDCOUINWEIUCNWNC'
#         count = 0
#         for char in word:
#             if char in consonants:
#                 count += 1
#         return count

# a = A()
# b = B()

# word = "hello"
# a_count = a.count(word)
# b_count = b.count(word)

# print(f"Number of vowels in '{word}': {a_count}")
# print(f"Количество согласных в '{word}': {b_count}")




