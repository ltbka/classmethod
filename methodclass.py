"""
1)Создайте класс MathUtils с staticmethod под названием multiply,
который принимает два аргумента и возвращает их произведение.
"""
# class MathUtils:
#     @staticmethod
#     def multiply(a, b):
#         return a * b

# result = MathUtils.multiply(2, 3)
# print(result)

"""
2)Создайте класс DateUtils с classmethod под названием is_valid_date, 
который принимает строку в формате даты (например, "2023-07-18") и проверяет, является ли эта дата действительной.
Метод должен возвращать True, если дата действительна, и False в противном случае.
"""

# class DateUtils():
#         @classmethod
#         def is_valid_date(cls,date_string):
#                 years = date_string.split('-')[-1]
#                 month = date_string.split('-')[-1]
#                 day = date_string.split('-')[-1]
#                 if int(years) > 0 and  int(month) <=15 and  int(month) > 0 and  int(day)>0 and int(day)<=28:
#                         return True
#                 else:
#                         return False
# date = DateUtils()

# print(date.is_valid_date('2022-13-7'))

"""
3)Создайте класс StringUtils с staticmethod под названием is_palindrome, который принимает строку и проверяет,
является ли она палиндромом (читается одинаково слева направо и справа налево).
Метод должен возвращать True, если строка является палиндромом, и False в противном случае
"""
# class StringUtils:
#     @staticmethod
#     def is_palindrome(string):
#         string = string.replace(" ", "")
#         string = string.lower()
#         if string == string[::-1]:
#             return True
#         else:
#             return False

# string = StringUtils()
# print(string.is_palindrome('awa'))

"""
4)Создайте класс Shape с staticmethod под названием get_circle_area,
который принимает радиус и возвращает площадь круга. Площадь круга вычисляется по формуле πr^2,
где π примерно равно 3.14159
"""
# class Shape:
#     @staticmethod
#     def get_circle_area(radius):
#         pi = 3.14159
#         area = pi * (radius ** 2)
#         return area
# radius = 5
# circle_area = Shape.get_circle_area(radius)
# print('Площадь круга:', circle_area)

"""
5)Создайте класс FileUtils с classmethod под названием get_file_extension,
который принимает имя файла в виде строки и возвращает его расширение. 
Если файл не имеет расширения, метод должен возвращать пустую строку.
Например, для файла "document.txt" метод должен вернуть ".txt
"""
# class FileUtils:
#     @classmethod
#     def get_file_extension(cls, file_name):
#         extension = ''
#         if '.' in file_name:
#             extension = file_name[file_name.rindex('.'):]
#         return extension
    
# file_name = "document.txt"
# file_extension = FileUtils.get_file_extension(file_name)
# print("Расширение файла:", file_extension)
 


