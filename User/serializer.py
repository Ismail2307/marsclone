from rest_framework import serializers
from models import  *


class StudentSRL(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = "__all__"
    
    
    
class LoginSRL(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['login', 'password']
    
class TeacherLoginSRL(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['login', 'password']
    
class TeacherSRL(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['login', 'password']
    
class GroupSRL(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ['login', 'password']
    
class HomeworkSRL(serializers.ModelSerializer):
  class Meta:
    model = Homework
    fields = "__all__"