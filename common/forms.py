from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# [21-12-14] username,pw1,pw2(UserCreationForm로 부터 상속) 와 email속성을 추가함
class UserForm(UserCreationForm) :
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")