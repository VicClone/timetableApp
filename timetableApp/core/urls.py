from django.conf.urls import url
from .views import UserView, UserRegisterView, UserAuthView, Logout

urlpatterns = [
    url(r'^login', UserAuthView.as_view()),
    url(r'^logout', Logout.as_view()),
    url(r'^register', UserRegisterView.as_view()),
    url(r'^user', UserView.as_view()),
]