from django.contrib import admin
from .models import *

# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    """ Занятие """

    list_display = ('time', 'group', 'teacher', 'day_week', 'discipline', 'auditurium')

admin.site.register(Lesson, LessonAdmin)


class AudituriumAdmin(admin.ModelAdmin):
    """ Аудитория """

    list_display = ('name', 'capacity', 'shedule')

admin.site.register(Auditurium, AudituriumAdmin)


class AudituriumScheduleAdmin(admin.ModelAdmin):
    """ Расписания аудиторий """

    list_display = ('auditurium', 'lesson_time', 'business')

admin.site.register(AudituriumSchedule, AudituriumScheduleAdmin)


class DisciplineAdmin(admin.ModelAdmin):
    """ Дисциплина """

    list_display = ('name',)

admin.site.register(Discipline, DisciplineAdmin)


class TeacherAdmin(admin.ModelAdmin):
    """ Преподаватель """

    list_display = ('name', 'discipline', 'shedule')

admin.site.register(Teacher, TeacherAdmin)


class TeacherScheduleAdmin(admin.ModelAdmin):
    """ Преподаватель """

    list_display = ('teacher', 'lesson_time', 'business')

admin.site.register(TeacherSchedule, TeacherScheduleAdmin)


class GroupAdmin(admin.ModelAdmin):
    """ Группа """

    list_display = ('name', 'people_count', 'max_lessons', 'max_repeat_lessons', 'shedule')

admin.site.register(Group, GroupAdmin)


class GroupSheduleAdmin(admin.ModelAdmin):
    """ Расписание группы """

    list_display = ('group', 'lesson_time', 'business')

admin.site.register(GroupShedule, GroupSheduleAdmin)


class GroupWorkloadAdmin(admin.ModelAdmin):
    """ Занятость группы """

    list_display = ('group', 'discipline', 'amount')

admin.site.register(GroupWorkload, GroupWorkloadAdmin)


class TimeLessonAdmin(admin.ModelAdmin):
    """ Время """

    list_display = ('number', 'start', 'end', 'shedule')

admin.site.register(TimeLesson, TimeLessonAdmin)


class SheduleAdmin(admin.ModelAdmin):
    """ Расписание """

    list_display = ('user', 'fourth', 'period', 'date')
    # list_display = ('user', 'name', 'shedule_lesson', 'date')
    
    # def shedule_lesson(self, obj):
    #     print(obj.lessons.all())
    #     return "\n".join([str(lesson.number) for lesson in obj.lessons.all()])

admin.site.register(Shedule, SheduleAdmin)