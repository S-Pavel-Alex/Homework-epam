import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Class error"""
    pass


class People:
    def __init__(self, first_name: str, last_name: str):
        """
        Class description first and last name for the teacher and student
        :param first_name: first name
        :type first_name: str
        :param last_name: last name
        :type last_name: str
        """
        self.first_name = first_name
        self.last_name = last_name


class HomeworkResult:
    def __init__(self, author: "Student", homework, solution: str):
        """
        Constructor method for Homework class
        :param author: object who do homework
        :type author: Student
        :param homework: object homework
        :type homework: object
        :param solution: answer's text
        :type solution: str
        :raises TypeError: You gave a not Homework object
        """
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
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

    def is_active(self) -> bool:
        """
        Checks if the time for the task has expired
        :return: bool
        """
        return datetime.datetime.now() < self.created + self.deadline


class Teacher(People):
    """
    Class which check homework result and add in dict
    """
    homework_done = defaultdict(str)

    @staticmethod
    def check_homework(homework_result: object()) -> bool:
        """
        Method check homework result, how many symbols in result and
        add in homework done if all alright
        :param homework_result: object with result
        :type homework_result: object()
        :return: bool
        """
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework] = \
                homework_result.solution
            return True
        else:
            return False

    @staticmethod
    def reset_results(homework=None):
        """
        Method which delete homework from homework done, if homework in and
        clean homework done if non homework
        :param homework: object with homework text
        :type homework: None or object
        """
        if isinstance(homework, Homework):
            del Teacher.homework_done[homework]
        elif homework is None:
            Teacher.homework_done.clear()

    @staticmethod
    def create_homework(text: str, how_many_days: int) -> object:
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
    def do_homework(self, homework: object(), solution: str) -> object:
        """
        :param homework: object Homework's class
        :type homework: object()
        :param solution: answer's text
        :type solution: str
        :raise DeadlineError: You are late
        :return: object if homework.is_active is True
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError('You are late')
