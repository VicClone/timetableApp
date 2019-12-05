import uuid
from django.db import models
# Create your models here.


class Auditurium(models.Model):
    """ Модель аудитории """

    name = models.CharField(primary_key=True, verbose_name="Название", max_length=25)
    address = models.CharField(verbose_name="Адрес", max_length=100)

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"


class Discipline(models.Model):
    """ Модель дисциплины """

    did = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(primary_key=True, verbose_name="Название", max_length=25)

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class Teacher(models.Model):
    """ Модель преподавателя """

    tid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(primary_key=True, verbose_name="Имя", max_length=50)
    workload = models.FloatField(verbose_name="Нагрузка")
    discipline = models.ForeignKey(Discipline, verbose_name="Профиль", on_delete = models.CASCADE)
    auditurium = models.ForeignKey(Auditurium, verbose_name="Аудитория", on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Group(models.Model):
    """ Модель группы """

    gid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(primary_key=True, verbose_name="Название", max_length=25)
    workload = models.FloatField(verbose_name="Нагрузка")
    people_count = models.IntegerField(verbose_name="Количество учащихся")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Lesson(models.Model):
    """ Модель занятия """

    lid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson_number = models.IntegerField(verbose_name="Номер занятия")
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE, )
    day = models.IntegerField(verbose_name="День")
    data = models.DateField(verbose_name="дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"