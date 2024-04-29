from django.urls import path
from views import *

urlpatterns = [
    path("student/register", RegisterView.as_view()),
    path("student/login", LoginView.as_view()),
    path("teacher/register", TeacherRegisterView.as_view()),
    path("teacher/login", TeacherLoginView.as_view()),
    path("group/create", GroupView.as_view()),
    path("group/edit<int:id>", EditGroupView.as_view()),   
    path("homework/",HomeworkView.as_view(),) 
]
