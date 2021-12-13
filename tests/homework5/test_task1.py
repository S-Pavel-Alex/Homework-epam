import datetime
import time

from homework5.task1 import (Homework, Student, Teacher)


def test_class_homework_text():
    homework = Homework('Test', 3)
    assert homework.text == 'Test'


def test_class_homework_deadline():
    homework = Homework('Test', 3)
    assert homework.deadline == datetime.timedelta(days=3)


def test_class_homework_is_active_positive():
    homework = Homework('Test', 3)
    assert homework.is_active() is True


def test_class_homework_is_active_negative():
    homework = Homework('Test', 0)
    assert homework.is_active() is False


def test_class_homework_is_active_negative_with_deadline_not_0():
    homework = Homework('Test', -2)
    assert homework.is_active() is False


def test_teacher_class():
    teacher = Teacher('Daniil', 'Shadrin')
    assert teacher.first_name == 'Daniil'
    assert teacher.last_name == 'Shadrin'


def test_student_class():
    student = Student('Bin', 'Bon')
    assert student.first_name == 'Bin'
    assert student.last_name == 'Bon'


def test_working_classes():
    student = Student('Roman', 'Petrov')
    teacher = Teacher('Daniil', 'Shadrin')
    expired_homework = teacher.create_homework('Learn functions', 0)
    assert expired_homework.text == 'Learn functions'
    active_homework = teacher.create_homework('Do something', 3)
    time.sleep(1)
    assert active_homework.text == 'Do something'
    assert student.do_homework(active_homework) == active_homework
    assert student.do_homework(expired_homework) is None
