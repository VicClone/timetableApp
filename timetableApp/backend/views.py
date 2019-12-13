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
        teachers = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response(serializer.data)

class AudituriumsView(APIView):
    """ Аудитории """

    def get(self, request):
        audituriums = Auditurium.objects.all()
        serializer = AudituriumSerializers(audituriums, many=True)
        return Response(serializer.data)

class GroupsView(APIView):
    """ Группы """

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializers(groups, many=True)
        return Response(serializer.data)


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