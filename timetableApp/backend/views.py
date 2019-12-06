from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView

# Create your views here.

""" from .models import Lesson
from .serializers import LessonSerializers
from .models import Teacher
from .serializers import TeacherSerializers
from .models import Auditurium
from .serializers import AudituriumSerializers """

from .models import *
from .serializers import *

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
        times = Time.objects.all()
        serializer = TimeSerializers(times, many=True)
        return Response(serializer.data)


class ShedulesView(APIView):
    """ Расписания """

    def get(self, request):
        shedules = Shedule.objects.all()
        serializer = SheduleSerializers(shedules, many=True)
        return Response({"data": serializer.data})

class SheduleUserView(APIView):
    """ Расписание пользователя """

    def get(self, request):
        userId = request.GET.get("userId")
        # print(Shedule.objects)    
        shedule = Shedule.objects.get(user=userId)
        serializer = SheduleUserSerializers(shedule)
        return Response({"data": serializer.data})