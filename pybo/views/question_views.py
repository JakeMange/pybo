from django.contrib import messages
# [21-12-13] 페이징 기능 구현
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
# from django.http import HttpResponse
from ..models import Question


# [21-12-07] /pybo/question_list.html의 url 매핑에 의해 실행될 question_create 함수
@login_required(login_url='common:login')
def question_create(request):
  # form = QuestionForm()
  # return render(request, 'pybo/question_form.html', {'form': form})

  if request.method == 'POST':
      form = QuestionForm(request.POST)
      if form.is_valid():
          question = form.save(commit=False)
          question.author = request.user
          question.create_date = timezone.now()
          question.save()
          return redirect('pybo:index')
  else:
      form = QuestionForm()
  context = {'form': form}
  return render(request, 'pybo/question_form.html', context)

# [21-12-14] 질문 수정 함수 추가
@login_required(login_url='common:login')
def question_modify(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   if request.user != question.author:
      messages.error(request, '수정 권한이 없습니다.')
      return redirect('pybo:detail', question_id=question_id)

   if request.method == "POST":
      # [21-12-14] 질문 수정 화면에 기존제목, 내용 반영
      form = QuestionForm(request.POST, instance=question)
      if form.is_valid():
          question = form.save(commit=False)
          question.author = request.user
          question.modify_date = timezone.now()
          question.save()
          return redirect('pybo:detail', question_id=question_id)
   else:
    form = QuestionForm(instance=question)
   context = {'form': form}
   return render(request, 'pybo/question_form.html', context)

# [21-12-14] 질문 삭제 함수 추가
@login_required(login_url='common:login')
def question_delete(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   if request.user != question.author:
      messages.error(request, '삭제 권한이 없습니다.')
      return redirect('pybo:detail', question_id=question_id)
   question.delete()
   return redirect('pybo:index')