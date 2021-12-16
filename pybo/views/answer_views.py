from django.contrib import messages
# [21-12-13] 페이징 기능 구현
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
# from django.http import HttpResponse
from ..models import Question, Answer


# [21-12-06]form 엘리먼트에 입력된 값을 받아 데이터베이스에 저장할 수 있도록 answer_create 함수를
# pybo/views.py 파일(detail함수)에 추가 (새로고침으로 이해)
# [21-12-07] 답변등록
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('pybo:detail', question_id=question_id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

# [21-12-14] 답변 수정 함수 추가
@login_required(login_url='common:login')
def answer_modify(request, answer_id):
   answer = get_object_or_404(Answer, pk=answer_id)
   if request.user != answer.author:
      messages.error(request, '수정 권한이 없습니다.')
      return redirect('pybo:detail', question_id=answer.question_id)

   if request.method == "POST":
      # [21-12-14] 질문 수정 화면에 기존제목, 내용 반영
      form = AnswerForm(request.POST, instance=answer)
      if form.is_valid():
          answer = form.save(commit=False)
          answer.author = request.user
          answer.modify_date = timezone.now()
          answer.save()
          return redirect('{}#answer_{}'.format(
              resolve_url('pybo:detail', question_id=answer.question_id), answer.id))
   else:
    form = AnswerForm(instance=answer)
   context = {'answer': answer, 'form': form}
   return render(request, 'pybo/answer_form.html', context)

# [21-12-14] 답변 삭제 함수 추가
@login_required(login_url='common:login')
def answer_delete(request, answer_id):
   answer = get_object_or_404(Answer, pk=answer_id)
   if request.user != answer.author:
      messages.error(request, '삭제 권한이 없습니다.')
   else:
      answer.delete()
   return redirect('pybo:detail', question_id=answer.question.id)

