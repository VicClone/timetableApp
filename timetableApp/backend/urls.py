from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^lessons', LessonsView.as_view()),
    url(r'^teachers', TeachersView.as_view()),
    url(r'^audituriums', AudituriumsView.as_view()),
    url(r'^shedules', ShedulesView.as_view()),
    url(r'^sheduleUser', SheduleUserView.as_view())
]