import pytest

from homework6.task2 import *


def test_class_teacher():
    teacher = Teacher('Pavel', 'Smirnov')
    assert teacher.first_name == 'Pavel'
    assert teacher.last_name == 'Smirnov'


def test_student_class():
    student = Student('Bin', 'Bon')
    assert student.first_name == 'Bin'
    assert student.last_name == 'Bon'


def test_working_classes(capsys):
    student = Student('Roman', 'Petrov')
    teacher = Teacher('Daniil', 'Shadrin')
    expired_homework = teacher.create_homework('Learn functions', 0)
    # assert expired_homework.text == 'Learn functions'
    # active_homework = teacher.create_homework('Do something', 3)
    # assert active_homework.text == 'Do something'
    # assert student.do_homework(active_homework) == active_homework
    with pytest.raises(DeadlineError) as error:
        student.do_homework(expired_homework)
    assert str(error.value) == 'You are late'


def test_homework_result_positive():
    homework = Homework('text task', 4)
    student = Student('Pavel', 'Smirnov')
    assert HomeworkResult('text task', 'good job', student)
    # assert isinstance(hw.author, Student)


def test_homework_result_negative():
    student = Student('Pavel', 'Smirnov')
    homework = Homework('super task', 4)
    with pytest.raises(ObjectUncorrected) as err:
        HomeworkResult('text task', 'good job', student)
    assert str(err.value) == 'You gave a not Homework object'

