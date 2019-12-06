from rest_framework import serializers
# from timetableApp.core.models import User
from timetableApp.core.serializers import UserSerializer

from .models import *

class LessonSerializers(serializers.ModelSerializer):
    """ Сериализация занятий """

    class Meta:
        model = Lesson
        fields = ('time', 'group', 'teacher')


class AudituriumSerializers(serializers.ModelSerializer):
    """ Сериализация аудиторий """

    class Meta:
        model = Auditurium
        fields = ('name', 'address')


class DisciplineSerializers(serializers.ModelSerializer):
    """ Сериализация дисциплин """

    class Meta:
        model = Discipline
        fields = ('name',)


class TeacherSerializers(serializers.ModelSerializer):
    """ Сериализация преподавателей """

    class Meta:
        model = Teacher
        fields = ('name', 'workload', 'discipline', 'auditurium')


class GroupSerializers(serializers.ModelSerializer):
    """ Сериализация групп """

    class Meta:
        model = Group
        fields = ('name', 'workload', 'people_count')


class TimeLessonSerializers(serializers.ModelSerializer):
    """ Сериализация звонков """

    class Meta:
        model = TimeLesson
        fields = ('number', 'start', 'end', 'breaks', 'day_week')


class SheduleSerializers(serializers.ModelSerializer):
    """ Сериализация расписания """
    # lessons = LessonSerializers()
    user = UserSerializer()

    class Meta:
        model = Shedule
        fields = ('user', 'name', 'lessons', 'date')

class SheduleUserSerializers(serializers.ModelSerializer):
    """ Сериализация расписания """
    # lessons = LessonSerializers()
    # user = UserSerializer()

    class Meta:
        model = Shedule
        fields = ('user', 'name', 'lessons', 'date')
