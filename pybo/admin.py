from django.contrib import admin
from .models import Question

# [21-12-03] p72 장고 Admin에서 모델 관리하기 ,검색기능 추가-----------------#
class QuestionAdmin(admin.ModelAdmin) :
    search_fields = ['subject']

# [21-12-03] p72 장고 Admin에서 모델 관리하기 ,등록-----------------#
admin.site.register(Question, QuestionAdmin)