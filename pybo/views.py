from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm, AnswerForm

def index(request):
    # [21-12-03] pybo 목록 출력: 작성 날짜의 역순
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영 합니다.12-02 시작")
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # [21-12-03] pypo 내용 출력 : urls.py에 있는  path('<int:question_id>/', views.detail),과 연결
    # question = Question.objects.get(id=question_id) ,없는 페이지를 반환 할때 에러 처리가 필요하다.
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

# [21-12-06]form 엘리먼트에 입력된 값을 받아 데이터베이스에 저장할 수 있도록 answer_create 함수를
# pybo/views.py 파일(detail함수)에 추가 (새로고침으로 이해)
# [21-12-07] 답변등록
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

# [21-12-07] /pybo/question_list.html의 url 매핑에 의해 실행될 question_create 함수
def question_create(request):
  # form = QuestionForm()
  # return render(request, 'pybo/question_form.html', {'form': form})

  if request.method == 'POST':
      form = QuestionForm(request.POST)
      if form.is_valid():
          question = form.save(commit=False)
          question.create_date = timezone.now()
          question.save()
          return redirect('pybo:index')
  else:
      form = QuestionForm()
  context = {'form': form}
  return render(request, 'pybo/question_form.html', context)