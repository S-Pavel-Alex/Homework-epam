import datetime

import pytest
from freezegun import freeze_time

from homework6.task2 import (DeadlineError, Homework, HomeworkResult, Student,
                             Teacher)


def test_class_teacher():
    teacher_good = Teacher('Pavel', 'Smirnov')
    good_hw = teacher_good.create_homework("It's good task", 2)
    good_student = Student('Spider', 'Man')
    good_result = HomeworkResult(good_student, good_hw, "It's is good answer")
    assert teacher_good.first_name == 'Pavel'
    assert teacher_good.last_name == 'Smirnov'
    assert teacher_good.check_homework(good_result) is True
    assert teacher_good.homework_done[good_hw] ==\
           ["It's is good answer"]


def test_teacher_class_bad():
    """Test about bad answer to the task"""
    teacher_bad = Teacher('Brad', 'Pitt')
    bad_hw = teacher_bad.create_homework("It's bad task", 2)
    bad_student = Student('Otto', 'Octavius')
    bad_result = HomeworkResult(bad_student, bad_hw, 'Done')
    assert teacher_bad.check_homework(bad_result) is False
    assert teacher_bad.homework_done[bad_hw] == []


def test_teacher_common():
    """Homework_done are common for all teachers"""
    teacher_one = Teacher('Brad', 'Pitt')
    teacher_two = Teacher('Iron', 'Man')
    teacher_three = Teacher('Super', 'Man')
    hw = teacher_one.create_homework('This is task', 2)
    student = Student('Spider', 'Man')
    result1 = student.do_homework(hw, 'This is result')
    result2 = student.do_homework(hw, 'This is result too')
    result3 = student.do_homework(hw, 'This is result again')
    teacher_one.check_homework(result1)
    teacher_two.check_homework(result2)
    teacher_three.check_homework(result3)
    assert teacher_one.homework_done == teacher_two.homework_done
    assert teacher_two.homework_done == teacher_three.homework_done


def test_reset_answer():
    """Check deleting one position"""
    teacher_good = Teacher('Pavel', 'Smirnov')
    good_hw = teacher_good.create_homework("It's good task", 2)
    good_hw2 = teacher_good.create_homework("It's good task", 2)
    good_hw3 = teacher_good.create_homework("It's good task", 2)
    good_student = Student('Spider', 'Man')
    good_result = HomeworkResult(good_student, good_hw, "It's is good answer")
    good_result1 = HomeworkResult(good_student, good_hw, "It's is good answer"
                                                         " for good student")
    good_result2 = HomeworkResult(good_student, good_hw2,
                                  "It's is good answer too")
    good_result3 = HomeworkResult(good_student, good_hw3,
                                  "It's is good answer again")
    teacher_good.check_homework(good_result)
    teacher_good.check_homework(good_result1)
    teacher_good.check_homework(good_result2)
    teacher_good.check_homework(good_result3)
    assert Teacher.homework_done[good_hw] == ["It's is good answer",
                                              "It's is good answer"
                                              " for good student"
                                              ]
    assert Teacher.homework_done[good_hw2] == ["It's is good answer too"]
    assert Teacher.homework_done[good_hw3] == ["It's is good answer again"]
    Teacher.reset_results(good_hw)
    assert Teacher.homework_done[good_hw] == []
    Teacher.reset_results()
    assert Teacher.homework_done == {}


def test_student_class_positive():
    """Test about homework is not expired"""
    student = Student('Bin', 'Bon')
    homework = Homework('Learn all what you want', 2)
    assert student.first_name == 'Bin'
    assert student.last_name == 'Bon'
    assert isinstance(student.do_homework(homework, 'This is good answer'),
                      HomeworkResult)


@freeze_time("30-12-21")
def test_student_class_negative():
    """Test about homework is expired"""
    student = Student('Bin', 'Bon')
    homework = Homework('Learn all what you want', 1)
    homework.created = datetime.datetime(2021, 12, 15)
    assert student.first_name == 'Bin'
    assert student.last_name == 'Bon'
    with pytest.raises(DeadlineError) as err:
        student.do_homework(homework, 'This is bad')
    assert str(err.value) == 'You are late'


def test_homework_class_positive_deadline():
    """Positive test because homework in deadline"""
    homework = Homework('Learn all what you want', 2)
    assert homework.text == 'Learn all what you want'
    assert homework.deadline == datetime.timedelta(days=2)
    assert homework.is_active() is True


@freeze_time("30-12-21")
def test_homework_class_negative_deadline():
    """Negative test because homework out deadline"""
    homework = Homework('Learn all what you want', 2)
    assert homework.text == 'Learn all what you want'
    assert homework.deadline == datetime.timedelta(days=2)
    homework.created = datetime.datetime(2021, 12, 21)
    assert homework.is_active() is False


def test_homework_result_positive():
    """Test with correct arguments"""
    homework_do = Homework('Learn all what you want', 2)
    student = Student('Bin', 'Bon')
    hw_result = HomeworkResult(student, homework_do, 'This is great hw')
    assert isinstance(homework_do, Homework)
    assert hw_result.solution == 'This is great hw'
    assert hw_result.homework == homework_do
    assert hw_result.author == student


def test_homework_result_negative():
    student = Student('Bin', 'Bon')
    with pytest.raises(TypeError) as err:
        HomeworkResult(student, "homework", 'This is great hw')
    assert str(err.value) == 'You gave a not Homework object'
