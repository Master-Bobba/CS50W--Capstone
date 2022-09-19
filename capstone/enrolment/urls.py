from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("timetable", views.timetable, name="timetable"),
    path("enrolment", views.enrolment, name="enrolment"),
    path('moodle', views.moodle, name="moodle")

]