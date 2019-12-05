from django.db import models

# Create your models here.

class Lesson(models.Model):
    """ Модель занятия """

    lid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auditurium = models.ForeignKey(Auditurium, verbose_name="Аудитория", on_delete=models.CASCADE)
    lesson_number = models.IntegerField(verbose_name="Номер занятия")
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    day = models.IntegerField(verbose_name="День")
    data = models.DateField(verbose_name="дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Занятие"


class Auditurium(models.Model):
    """ Модель аудитории """

    aid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Название")
    address = models.CharField(verbose_name="Адрес", max_length=100)

    class Meta:
        verbose_name = "Аудитория"


class Discipline(models.Model):
    """ Модель дисциплины """

    did = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Название", max_length=100)

    class Meta:
        verbose_name = "Дисциплина"


class Teacher(models.Model):
    """ Модель преподавателя """

    tid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Имя", max_length=100)
    workload = models.FloatField(verbose_name="Нагрузка")
    discipline = models.ForeignKey(Discipline, verbose_name="Профиль", on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Преподаватель"


class Group(models.Model):
    """ Модель группы """

    gid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Название", max_length=100)
    workload = models.FloatField(verbose_name="Нагрузка")
    people_count = models.IntegerField(verbose_name="Количество учащихся")

    class Meta:
        verbose_name = "Группа"

