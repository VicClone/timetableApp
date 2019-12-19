from rest_framework import serializers
from timetableApp.core.serializers import UserSerializer

from .models import *
from timetableApp.core.models import User

class AudituriumSerializers(serializers.ModelSerializer):
    """ Сериализация аудиторий """

    class Meta:
        model = Auditurium
        fields = ('name', 'address', 'capacity')

class AudituriumScheduleSerializers(serializers.ModelSerializer):
    """ Сериализация расписаний аудиторий """

    class Meta:
        model = Auditurium
        fields = ('auditurium', 'lesson_time', 'business')


class DisciplineSerializers(serializers.ModelSerializer):
    """ Сериализация дисциплин """

    class Meta:
        model = Discipline
        fields = ('did', 'name', 'shedule')

class DisciplinePostSerializers(serializers.ModelSerializer):
    """ Сериализация дисциплин """

    class Meta:
        model = Discipline
        fields = ('name',)


class TeachersSerializers(serializers.ModelSerializer):
    """ Сериализация преподавателей """

    class Meta:
        model = Teacher
        fields = ('name', 'discipline', 'shedule')


class TeacherPostSerializers(serializers.ModelSerializer):
    """ Добавление преподавателей """

    class Meta:
        model = Teacher
        fields = ('name',)


class TeacherSchedulesSerializers(serializers.ModelSerializer):
    """ Сериализация расписания преподавателей """

    class Meta:
        model = TeacherSchedule
        fields = ('teacher', 'lesson_time', 'business')


class GroupSerializers(serializers.ModelSerializer):
    """ Сериализация групп """

    class Meta:
        model = Group
        fields = ('gid', 'name', 'people_count', 'max_lessons', 'max_repeat_lessons', 'shedule')

class GroupPostSerializers(serializers.ModelSerializer):
    """ Сериализация групп """

    class Meta:
        model = Group
        fields = ('name', 'people_count', 'max_lessons', 'max_repeat_lessons')


class GroupSheduleSerializers(serializers.ModelSerializer):
    """ Сериализация расписания групп """

    class Meta:
        model = GroupShedule
        fields = ('group', 'lesson_time', 'business')


class GroupWorkloadSerializers(serializers.ModelSerializer):
    """ Сериализация нагрузки групп """

    class Meta:
        model = GroupWorkload
        fields = ('group', 'discipline', 'amount')

class GroupWorkloadPostSerializers(serializers.ModelSerializer):
    """ Добавление нагрузки групп """

    class Meta:
        model = GroupWorkload
        fields = ('amount',)


class TimeSerializers(serializers.ModelSerializer):
    """ Сериализация звонков """

    class Meta:
        model = TimeLesson
        fields = ('number', 'start', 'end', 'day_week', 'shedule')

class TimePostSerializers(serializers.ModelSerializer):
    """ Сериализация добавления звонков """

    class Meta:
        model = TimeLesson
        fields = ('number', 'start', 'end', 'day_week')


class SheduleSerializers(serializers.ModelSerializer):
    """ Сериализация расписания """
    # lessons = LessonSerializers()
    user = UserSerializer()

    class Meta:
        model = Shedule
        fields = ('user', 'fourth', 'period', 'date')

class LessonSerializers(serializers.ModelSerializer):
    """ Сериализация занятий """
    shedule = SheduleSerializers()

    class Meta:
        model = Lesson
        fields = ('time', 'shedule', 'group', 'teacher')


class SheduleUserSerializers(serializers.ModelSerializer):
    """ Сериализация расписания """
    user = UserSerializer()

    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Shedule
        fields = ('sid', 'user', 'fourth', 'period', 'date', 'lessons')

    def get_lessons(self, obj):
        return [LessonSerializers(el).data for el in Lesson.objects.filter(shedule=obj).all()]


class ShedulePostSerializers(serializers.ModelSerializer):
    """ Добавление расписания """
    
    class Meta:
        model = Shedule
        fields = ('fourth', 'period')