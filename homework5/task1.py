"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    def __init__(self, text: str, deadline: int):
        """
        Constructor method for Homework class
        :param text: task's text
        :type text: str
        :param deadline: how many days for your task
        :type deadline: int
        """
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        """
        Checks if the time for the task has expired
        :return: bool
        """
        return datetime.datetime.now() < self.created + self.deadline


class Teacher:
    def __init__(self, first_name: str, last_name: str):
        """
        Constructor method for Teacher class
        :param first_name: teacher's first name
        :type first_name: str
        :param last_name: teacher's last name
        :type last_name: str
        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, how_many_days: int):
        """
        Create and return new Homework instance
        :param text: task's text
        :type text: str
        :param how_many_days: how many days for task
        :type how_many_days: int
        :return: new Homework instance
        """
        return Homework(text, how_many_days)


class Student:
    def __init__(self, first_name: str, last_name: str):
        """
        Constructor method for Student class
        :param first_name: Student's first name
        :type first_name: str
        :param last_name: Student's last name
        :type last_name: str
        """
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: object()):
        """

        :param homework: object Homework's class
        :type homework: object()
        :return: object if homework.is_active is True and None if False and
        print You are lost
        """
        if homework.is_active():
            return homework
        else:
            print('You are lose')
            return None
