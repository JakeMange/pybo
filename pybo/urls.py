from django.urls import path
from . import views
from django.urls import path, include
from .views import base_views, question_views, answer_views, comment_views, vote_views

# [21-12-06] pybo/urls.py 파일에 네임 스페이스 추가
app_name = 'pybo'

urlpatterns = [
    path('', base_views.index, name='index'),
    # [21-12-03] url 경로 오류시 views.py와 url 연결 추가하기
    path('<int:question_id>/', base_views.detail, name='detail'),
    # [21-12-06] 사용자가 상세 화면에서〈질문답변〉버튼을 눌렀을 때 작동할
    # form 엘리먼트의 /pybo/answer/create/2/에 대한 URL 매핑을 추가한 것
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    # [21-12-14] 질문 수정 버튼 url 매핑
    path('question/modify/<int:question_id>/', views.question_modify,
         name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete,
         name='question_delete'),
    # [21-12-14] 답변 수정 버튼 url 매핑
    path('answer/modify/<int:answer_id>/', views.answer_modify,
         name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete,
         name='answer_delete'),
    # [21-12-15] 질문 댓글
    path('comment/create/question/<int:question_id>/', views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question,
         name='comment_delete_question'),
    # [21-12-15] 답변 댓글
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer,
         name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer,
         name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer,
         name='comment_delete_answer'),
    # [21-12-15] vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question,
         name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer,
         name='vote_answer'),
]
