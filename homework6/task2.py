from collections import defaultdict
import datetime



class DeadlineError(Exception):
    pass


class ObjectUncorrected(Exception):
    pass


class People:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class HomeworkResult:
    def __init__(self, homework, solution: str, author: "Student"):
        if not isinstance(homework, Homework):
            raise ObjectUncorrected('You gave a not Homework object')
        self.homework = homework
        self.author = author
        self.solution = solution
        self. create = datetime.datetime.now()


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


class Teacher(People):
    homework_done = defaultdict
    def  check_homework(self, homework_result):


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


class Student(People):
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
            raise DeadlineError('You are late')
