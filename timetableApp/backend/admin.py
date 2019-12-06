from django.contrib import admin
from .models import *

# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    """ Занятие """

    list_display = ('number', 'time', 'group', 'teacher')

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


class TimeLessonAdmin(admin.ModelAdmin):
    """ Время """

    list_display = ('number', 'start', 'end', 'breaks', 'day_week')

admin.site.register(TimeLesson, TimeLessonAdmin)


class SheduleAdmin(admin.ModelAdmin):
    """ Расписание """

    list_display = ('user', 'name', 'shedule_lesson', 'date')
    
    def shedule_lesson(self, obj):
        print(obj.lessons.all())
        return "\n".join([str(lesson.number) for lesson in obj.lessons.all()])

admin.site.register(Shedule, SheduleAdmin)