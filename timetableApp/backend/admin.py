from django.contrib import admin
from .models import Lesson
from .models import Auditurium
from .models import Discipline
from .models import Teacher
from .models import Group

# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    """ Занятие """

    list_display = ('lesson_number', 'group', 'teacher', 'day')

admin.site.register(Lesson, LessonAdmin)

class AudituriumAdmin(admin.ModelAdmin):
    """ Аудитория """

    list_display = ('name', 'address')

admin.site.register(Auditurium, AudituriumAdmin)


class DisciplineAdmin(admin.ModelAdmin):
    """ Дисциплина """

    list_display = ('name',)

admin.site.register(Discipline, DisciplineAdmin)


class TeacherAdmin(admin.ModelAdmin):
    """ Преподаватель """

    list_display = ('name', 'workload', 'discipline', 'auditurium')

admin.site.register(Teacher, TeacherAdmin)


class GroupAdmin(admin.ModelAdmin):
    """ Группа """

    list_display = ('name', 'workload', 'people_count')

admin.site.register(Group, GroupAdmin)