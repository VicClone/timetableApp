import uuid
from django.db import models
from timetableApp.core.models import User
# Create your models here.


class Shedule(models.Model):
    """ Модель расписание """

    sid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, null=True)
    fourth = models.IntegerField(verbose_name="Четверть", default=0)
    period = models.CharField(verbose_name="Период", default='None', max_length=10)
    date = models.DateField(verbose_name="дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"


class Discipline(models.Model):
    """ Модель дисциплины """

    did = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Название", max_length=100)
    shedule = models.ForeignKey(Shedule, verbose_name="Расписание", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class TimeLesson(models.Model):
    """ Модель звонков """

    tid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(verbose_name="Номер занятия")
    start = models.TimeField(verbose_name="Начало")
    end = models.TimeField(verbose_name="Конец")
    day_week = models.IntegerField(verbose_name="День недели")
    shedule = models.ForeignKey(Shedule, verbose_name="Расписание", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Звонок"
        verbose_name_plural = "Звонки"


class Auditurium(models.Model):
    """ Модель аудитории """

    name = models.CharField(primary_key=True, verbose_name="Название", max_length=25)
    address = models.CharField(verbose_name="Адрес", max_length=100)
    capacity = models.IntegerField(verbose_name="Вместимость", default=0)

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"

class AudituriumSchedule(models.Model):
    """ Модель расписания аудитории """

    asid = models.UUIDField(default=uuid.uuid4, editable=False)
    auditurium = models.ForeignKey(Auditurium, verbose_name="Аудитория", on_delete=models.CASCADE, null=True)
    lesson_time = models.ForeignKey(TimeLesson, verbose_name="Время урока", on_delete=models.CASCADE, null=True)
    business = models.BooleanField(verbose_name="Занятость", default=False)

    class Meta:
        verbose_name = "Расписание аудитории"
        verbose_name_plural = "Расписания аудитории"


class Teacher(models.Model):
    """ Модель преподавателя """

    tid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(primary_key=True, verbose_name="Имя", max_length=50)
    discipline = models.ForeignKey(Discipline, verbose_name="Профиль", on_delete = models.CASCADE)
    shedule = models.ForeignKey(Shedule, verbose_name="Расписание", on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class TeacherSchedule(models.Model):
    """ Модель расписания группы """

    tsid = models.UUIDField(default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE, null=True)
    lesson_time = models.ForeignKey(TimeLesson, verbose_name="Время урока", on_delete=models.CASCADE, null=True)
    business = models.BooleanField(verbose_name="Занятость", default=False)

    class Meta:
        verbose_name = "Расписание преподавателей"
        verbose_name_plural = "Расписания преподавателей"


class Group(models.Model):
    """ Модель группы """

    gid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Название", max_length=25)
    people_count = models.IntegerField(verbose_name="Количество учащихся", default=0)
    max_lessons = models.IntegerField(verbose_name="Максимум занятий", default=0)
    max_repeat_lessons = models.IntegerField(verbose_name="Максимум одинаковых занятий", default=0)
    shedule = models.ForeignKey(Shedule, verbose_name="Расписание", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class GroupShedule(models.Model):
    """ Модель расписания группы """

    gsid = models.UUIDField(default=uuid.uuid4, editable=False)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE, null=True)
    lesson_time = models.ForeignKey(TimeLesson, verbose_name="Время урока", on_delete=models.CASCADE, null=True)
    business = models.BooleanField(verbose_name="Занятость", default=False)

    class Meta:
        verbose_name = "Расписание групп"
        verbose_name_plural = "Расписания групп"

    

class GroupWorkload(models.Model):
    """ Модель загруженность группы """

    gwid = models.UUIDField(default=uuid.uuid4, editable=False)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE, null=True)
    discipline = models.ForeignKey(Discipline, verbose_name="Дисциплина", on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(verbose_name="Количество уроков в неделю", default=0)

    class Meta:
        verbose_name = "Загруженность групп"
        verbose_name_plural = "Загруженности групп"


class Lesson(models.Model):
    """ Модель занятия """

    lid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(verbose_name="Номер", default=0)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE)
    time = models.ForeignKey(TimeLesson, verbose_name="Звонок", on_delete=models.CASCADE, null="True")
    shedule = models.ForeignKey(Shedule, verbose_name="Расписание", on_delete=models.CASCADE, null="True")

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"