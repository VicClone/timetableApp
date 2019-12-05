from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.

from .models import Lesson
from .serializers import LessonSerializers
from .models import Teacher
from .serializers import TeacherSerializers
from .models import Auditurium
from .serializers import AudituriumSerializers

class Lesson(APIView):
    """ Уроки """

    def get(self, request):
        lessons = Lesson.objects.all()
        serializer = LessonSerializers(lessons, many=True)
        return Response(serializer.data)

class Teacher(APIView):
    """ Преподаватели """

    def get(self, request):
        lessons = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response(serializer.data)

class Auditurium(APIView):
    """ Аудитории """

    def get(self, request):
        lessons = Auditurium.objects.all()
        serializer = AudituriumSerializers(teachers, many=True)
        return Response(serializer.data)