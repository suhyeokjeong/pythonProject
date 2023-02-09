# class SoccerPlayer(object):
#     def __init__(self, name, position, back_number):
#         self.name = name
#         self.position = position
#         self.back_number = back_number
#
#     def change_back_number(self, new_number):
#         print("선수의 등번호를 변경한다. From %d to %d" % (self.back_number, new_number))
#         self.back_number = new_number
#
# jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
#
# print("현재 선수의 등번호는: ", jinhyun.back_number)
# jinhyun.change_back_number(15)
# print("현재 선수의 등번호는: ", jinhyun.back_number)
#

# class Note(object):
#     def __init__(self, contents = None):
#         self.contents = contents
#
#     def write_contents(self, contents):
#         self.contents = contents
#
#     def romove_all(self):
#         self.contents = ""
#
#     def __str__(self):
#         return self.contents
#
# class NoteBook(object):
#     def __init__(self, title):
#         self.title = title
#         self.page_number = 1
#         self.notes = {}
#
#     def add_note(self, note, page = 0):
#         if self.page_number < 300:
#             if page == 0:
#                 self.notes[self.page_number] = note
#                 self.page_number +=1
#
#             else:
#                 self.notes = {page : note}
#                 self.page_number += 1
#
#         else:
#             print("페이지가 모두 채워졌다.")
#
#     def remove_note(self, page_number):
#         if page_number in self.notes.keys():
#             return self.notes.pop(page_number)
#         else:
#             print("해당 페이지는 존재하지 않는다")
#
#     def get_number_of_pages(self):
#         return len(self.notes.keys())


# class Person(object):
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def about_me(self):
#         print(f"저의 이름은, {self.name} 이고요, 제 나이는 {self.age}살입니다.")
#
# class Employee(Person):
#     def __init__(self, name, age, gender, salary, hire_date):
#         super().__init__(name, age, gender)
#         self.salary = salary
#         self.hire_date = hire_date
#
#     def do_work(self):
#         print("열심히 일을한다.")
#
#     def about_me(self):
#         super().about_me()
#         # 오버라이딩
#         print(f"제 급여는, {self.salary}원이고, 제 입사일은 {self.hire_date}입니다.")
#
# class Korean(Employee):
#     pass
#
# first_korean = Korean("Sungchul", 35, "Male", 10000, "2023-01-01")
#
#
# print(first_korean)
# print(first_korean.name)
# print(first_korean.age)
# print(first_korean.gender)
# print(first_korean.salary)
# first_korean.about_me()
# print(type(first_korean.about_me()))


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        # 자식 클래스만 함수 사용 가능
        raise NotImplementedError("Subclass must implement abstract method")
#
class Cat(Animal):
    def talk(self):
        return 'Meow!'
#
# class Dog(Animal):
#     def talk(self):
#         return "Woof! Woof!"
#
# animals = [Cat("Missy"), Cat("Mr.Mistoffelees"), Dog("Lassie")]
#
# # 부모의  이름으로 묶어서
# for animal in animals:
#     print(animal.name + ':' + animal.talk())
#
#
class Product(object):
    def __init__(self, name):
        self.name = name

    # @property
    # def name(self):
    #     return self.name

# class 1. __item 활용하여 정보 은닉 (Private variable)
class Inventory(object):
    def __init__(self):
        #정보 은닉?
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)


book = Product("book")
pencil = Product("pencil")
mouse = Product("mouse")
Miki = Cat("Miki")

my_inventory = Inventory()
my_inventory.add_new_item(book)
my_inventory.add_new_item(pencil)
# my_inventory.add_new_item(Product())
# my_inventory.add_new_item(Product())
# Invalid Item
# my_inventory.add_new_item(Miki)

print(my_inventory.get_number_of_items())

# # 정보 은닉되어 사용하지 못함
# my_inventory.__items

print(my_inventory.items)
my_inventory.items.append(mouse)
print(my_inventory.items)

# # 인벤토리에 있는 product name을 출력할수는없는가?
# for product in my_inventory:
#     print(product.name)
