from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

# Create your views here.

from .models import *
from .serializers import *
from timetableApp.core.models import User
from .algorithm import TimetableCreator, Lesson as LessonA, Room, Rooms, Teacher as TeacherA, Calendar, Teachers as TeachersA, Class

class LessonsView(APIView):
    """ Уроки """

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializers(lessons, many=True)
        return Response(serializer.data)

class TeachersView(APIView):
    """ Преподаватели """

    def get(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        teachers = Teacher.objects.filter(shedule=shedule[0])
        serializer = TeachersSerializers(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        disciplineId = request.GET.get("disciplineId")
        discipline = Discipline.objects.filter(did=disciplineId)
        teacher = TeacherPostSerializers(data=request.data)
        if teacher.is_valid():
            teacher.save(shedule=shedule[0], discipline=discipline[0])
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class TeacherShedulesView(APIView):
    """ Расписание преподавателя """
    def get(self, request):
        teacherId = request.GET.get("teacherId")
        teacher = Teacher.objects.filter(tid=teacherId)
        teacherSchedules = TeacherSchedule.objects.filter(teacher=teacher[0])
        serializer = TeacherSchedulesSerializers(teacherSchedules, many=True)
        return Response(serializer.data)

    def post(self, request):
        teacherId = request.GET.get("teacherId")
        teacher = Teacher.objects.filter(tid=teacherId)
        timeId = request.GET.get("timeId")
        time = TimeLesson.objects.filter(tid=timeId)
        teacherSchedules = TeacherSchedulePostSerializers(data=request.data)
        if discipline.is_valid():
            discipline.save(shedule=shedule[0], time=time[0])
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})
    

class AudituriumsView(APIView):
    """ Аудитории """

    def get(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        audituriums = Auditurium.objects.filter(shedule=shedule[0])
        serializer = AudituriumSerializers(audituriums, many=True)
        return Response(serializer.data)

    def post(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        auditurium = AudituriumPostSerializers(data=request.data)
        if auditurium.is_valid():
            auditurium.save(shedule=shedule[0])
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class DisciplineView(APIView):
    """ Дисциплины """

    def get(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        disciplines = Discipline.objects.filter(shedule=shedule[0])
        serializer = DisciplineSerializers(disciplines, many=True)
        return Response(serializer.data)

    def post(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        discipline = DisciplinePostSerializers(data=request.data)
        if discipline.is_valid():
            discipline.save(shedule=shedule[0])
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class GroupsView(APIView):
    """ Группы """

    def get(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        groups = Group.objects.filter(shedule=shedule[0])
        serializer = GroupSerializers(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        group = GroupPostSerializers(data=request.data)
        if group.is_valid():
            group.save(shedule=shedule[0])
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class GroupWorkloadView(APIView):
    """ Нагрузка группы """

    def get(self, request):
        groupId = request.GET.get("groupId")
        group = Group.objects.filter(gid=groupId)
        workloads = GroupWorkload.objects.filter(group=group[0])
        serializer = GroupWorkloadSerializers(workloads, many=True)
        return Response(serializer.data)

    def post(self, request):
        groupId = request.GET.get("groupId")
        group = Group.objects.filter(gid=groupId)
        disciplineId = request.GET.get("disciplineId")
        discipline = Discipline.objects.filter(did=disciplineId)
        workload = GroupWorkloadPostSerializers(data=request.data)
        if workload.is_valid():
            workload.save(group=group[0], discipline=discipline[0])
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class TimesView(APIView):
    """ Звонки """

    def get(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        times = TimeLesson.objects.filter(shedule=shedule[0])
        serializer = TimeSerializers(times, many=True)
        return Response(serializer.data)

    def post(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        time = TimePostSerializers(data=request.data)
        if time.is_valid():
            time.save(shedule=shedule[0])
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class ShedulesView(APIView):
    """ Расписания """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        shedules = Shedule.objects.all()
        serializer = SheduleSerializers(shedules, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        shedule = ShedulePostSerializers(data=request.data)
        if shedule.is_valid():
            shedule.save(user=request.user)
            return Response({"status": "Add"})
        else:
            return Response({"status": "Error"})


class ShedulesUserView(APIView):
    """ Расписание пользователя """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        userId = request.GET.get("userId")
        user = User.objects.filter(pk=userId)
        shedules = Shedule.objects.filter(user=user[0])
        serializer = SheduleUserSerializers(shedules, many=True)
        return Response({"data": serializer.data})


class SheduleView(APIView):
    """ Расписания """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        serializer = SheduleSerializers(shedule)
        return Response({"data": serializer.data})


class GenerateSheduleView(APIView):
    """ Генератор расписания """

    def get(self, request):
        sheduleId = request.GET.get("sheduleId")
        shedule = Shedule.objects.filter(sid=sheduleId)
        lessons = Lesson.objects.filter(shedule=shedule[0]) 
        serializer = LessonSerializers(lessons, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        Lesson.objects.all().delete()

        sheduleId = request.GET.get("sheduleId")
        shedules = Shedule.objects.filter(sid=sheduleId)

        disciplines = Discipline.objects.filter(shedule=shedules[0])
        teachersSh = Teacher.objects.filter(shedule=shedules[0])
        groups = Group.objects.filter(shedule=shedules[0])
        auditoriums = Auditurium.objects.filter(shedule=shedules[0])

        LECTURE = 'lecture'
        PRACTICE = 'practice'
        LABORATORY = 'laboratory'
        TYPE_LESSON = (LECTURE, PRACTICE, LABORATORY)
        DAY_WEEK = ('пн', 'вт', 'ср', 'чт', 'пт')
        TIMES = ('8:00', '9:00', '10:00', '11:00', '12:00')

        d1 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        d2 ={
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }

        room1 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        room2 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        room3 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        room4 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        room5 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        room6 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }

        teacher_1 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        teacher_2 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        teacher_3 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        teacher_4 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        teacher_5 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }
        teacher_6 = {
            'пн': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'вт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'ср': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'чт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
            'пт': {
                '8:00': False,
                '9:00': False,
                '10:00': False,
                '11:00': False,
                '12:00': False
            },
        }

        teachersA = []
        workloadA = {}
        classes = []
        rooms = []

        for teacher in teachersSh:
            lesson = LessonA(str(teacher.discipline.did), [LECTURE])
            teachersA.append(TeacherA(name=str(teacher.tid), lesson=lesson, timetable=Calendar(teacher_1)))

        for discipline in disciplines:
            workloadA[LessonA(str(discipline.did), is_type=LECTURE)] = 3

        for group in groups:
            classes.append(
                Class(
                    name=str(group.gid),
                    count=group.people_count,
                    timetable=Calendar(d1),
                    workload=workloadA,
                    max_lsns_per_day=group.max_repeat_lessons,
                    max_lsn_per_day=group.max_lessons,
                )
            )

        for auditorium in auditoriums:
            rooms.append(Room(TYPE_LESSON, auditorium.capacity, name=str(auditorium.name), timetable=Calendar(room1)))
        teachersA = TeachersA(teachersA)
        rooms = Rooms(rooms)

        creator = TimetableCreator(rooms, teachersA, classes)
        creator.create()

        lessonShedule = LessonPostSerializers(data={})
        for _class_ in classes:
            # print(_class_.name, _class_.timetable)
            for dayWeek in _class_.timetable.data:
                for time in _class_.timetable.data[dayWeek]:
                    itemLesson = _class_.timetable.data[dayWeek][time]
                    if (itemLesson == False):
                        continue
                    print(itemLesson[0])

                    groups = Group.objects.filter(gid=_class_.name)
                    day_week=dayWeek
                    timeSh=time
                    print(uuid.UUID(str(itemLesson[1])), 'uuid')
                    disciplines = Discipline.objects.filter(did=uuid.UUID(str(itemLesson[1])).hex)
                    teachersSh = Teacher.objects.filter(tid=uuid.UUID(str(itemLesson[0])).hex)
                    auditoriums = Auditurium.objects.filter(name=itemLesson[2])
                    lessonShedule = LessonPostSerializers(data={})

                    if lessonShedule.is_valid():
                        lessonShedule.save(shedule=shedules[0], group=groups[0], day_week=day_week, time=timeSh, teacher=teachersSh[0], discipline=disciplines[0], auditurium=auditoriums[0])                        
                        # return Response({"status": "Add"})
                    else:
                        return Response({"error": "error"})
        
        return Response({"status": "Add"})

            # print(type(_class_.timetable.data.get("пн").get("8:00")[0]))
        
        correct_ = []
        wrong_positions = []
        for _class_ in classes:
            lesson_sum = 0
        for day_of_the_week in _class_.timetable.data.values():
            for i in day_of_the_week:
                if day_of_the_week.get(i) is not False:
                    lesson_sum += 1
        if sum(_class_.workload.values())!=lesson_sum:
            correct_.append(0)
            wrong_positions.append(_class_.name)
        else:
            correct_.append(1)
        return Response({"status": "post generate"})