from django.db import models


class People(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(People):
    pass


class Teacher(People):
    pass


class Homework(models.Model):
    text = models.TextField()
    created = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f'{self.text} {self.created} {self.deadline}'


class HomeworkResult(models.Model):
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    author = models.ForeignKey('Student', on_delete=models.CASCADE)
    solution = models.CharField(max_length=200)
    created = models.DateTimeField()

    def __str__(self):
        return f'{self.homework} {self.author} {self.solution}'
