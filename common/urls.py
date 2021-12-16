from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'
# urlpatterns = []
# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(), name='login'),
# ]

# [21-12-13] django.contib.auth앱의 LoginView 클래스 활용, views.py 파일 수정 필요 없음
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]