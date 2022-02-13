# from django.http import HttpResponse
from django.db.models import Q, Count
# [21-12-13] 페이징 기능 구현

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question
import logging
logger = logging.getLogger(__name__)


# [21-12-15] views.py 파일 분리
def index(request):
    logger.info("INFO 레벨로 출력")
    # [21-12-03] pybo 목록 출력: 작성 날짜의 역순
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영 합니다.12-02 시작")
    # [21-12-13] 페이징 기능 입력 인자, pybo 목록 출력
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recentd')

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-creat_date')
    else: # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()


    #페이징 처리 - 페이지당 10개씩 보여주기
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # [21-12-03] pypo 내용 출력 : urls.py에 있는  path('<int:question_id>/', views.detail),과 연결
    # question = Question.objects.get(id=question_id) ,없는 페이지를 반환 할때 에러 처리가 필요하다.
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
