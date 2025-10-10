class Student:
    def __init__(self, full_name, age, group_number, average_grade):
        self.full_name = full_name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def info(self):
        print(f"ФИО: {self.full_name}")
        print(f"Возраст: {self.age}")
        print(f"Номер группы: {self.group_number}")
        print(f"Средний балл: {self.average_grade}")

    def stipend(self):
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5:
            return 4000
        else:
            return 0

    def compare_stipend(self, other):
        my_stipend = self.stipend()
        other_stipend = other.stipend()

        if my_stipend > other_stipend:
            print(f'{self.full_name} получает большую стипендию ({my_stipend} руб.), чем {other.full_name} ({other_stipend} руб.)')
        elif my_stipend < other_stipend:
            print(f'{self.full_name} получает меньшую стипендию ({my_stipend} руб.), чем {other.full_name} ({other_stipend} руб.)')
        else:
            print(f'{self.full_name} и {other.full_name} получают одинаковую стипендию ({my_stipend} руб.)')


class Aspirant(Student):
    def __init__(self, full_name, age, group_number, average_grade, research_work):
        super().__init__(full_name, age, group_number, average_grade)
        self.research_work = research_work

    def stipend(self):
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5:
            return 6000
        else:
            return 0

    def info(self):
        super().info()
        print(f'Научная работа: {self.research_work}')


# Проверка работы

student1 = Student('Опря Анна-Мария Олеговна', 20, '5132704/30801', 5)
student2 = Student('Лясович София Денисовна', 19, '5132704/30003', 4)
aspirant1 = Aspirant('Понаморенко Софья Андреевна', 24, 'ASP-102', 5, 'Исследование маршрутизаторов')
aspirant2 = Aspirant('Субботин Фёдор Евгеньевич', 25, 'ASP-103', 4, 'Моделирование динамических систем')

print('------Информация о студентах------')
student1.info()
print(f'Стипендия: {student1.stipend()} руб.\n')

student2.info()
print(f'Стипендия: {student2.stipend()} руб.\n')

print('------Информация об аспирантах------')
aspirant1.info()
print(f'Стипендия: {aspirant1.stipend()} руб.\n')

aspirant2.info()
print(f'Стипендия: {aspirant2.stipend()} руб.\n')

print('------Сравнение стипендий------')
student1.compare_stipend(aspirant1)
student2.compare_stipend(aspirant2)

