from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

# Create your views here.

from .models import *
from .serializers import *
from timetableApp.core.models import User

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
        serializer = TeachersSerializers(disciplines, many=True)
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

class AudituriumsView(APIView):
    """ Аудитории """

    def get(self, request):
        audituriums = Auditurium.objects.all()
        serializer = AudituriumSerializers(audituriums, many=True)
        return Response(serializer.data)


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