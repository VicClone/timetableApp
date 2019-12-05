from rest_framework import serializers

from .models import Lesson
from .models import Auditurium
from .models import Discipline
from .models import Teacher
from .models import Group

class LessonSerializers(serializers.ModelSerializer):
    """ Сериализация занятий """

    class Meta:
        model: Lesson
        fields = ('lesson_number', 'group', 'teacher', 'day')


class AudituriumSerializers(serializers.ModelSerializer):
    """ Сериализация аудиторий """

    class Meta:
        model: Auditurium
        fields = ('name', 'address')


class DisciplineSerializers(serializers.ModelSerializer):
    """ Сериализация дисциплин """

    class Meta:
        model: Discipline
        fields = ('name',)


class TeacherSerializers(serializers.ModelSerializer):
    """ Сериализация преподавателей """

    class Meta:
        model: Teacher
        fields = ('name', 'workload', 'discipline', 'auditurium')


class GroupSerializers(serializers.ModelSerializer):
    """ Сериализация групп """

    class Meta:
        model: Group
        fields = ('name', 'workload', 'people_count')