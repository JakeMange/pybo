from django.db import models
from django.contrib.auth.models import User


# [21-12-14] answer.author = request.user에서 User 대신
# AnonymousUser가 대입되어 오류가 발생방지 위해 어노테이션 추가

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    # [21-12-14] Question 모델에 author(글쓴이) 필드 추가하기
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    create_date = models.DateTimeField()
    # [21-12-14]질문, 답변을 언제 수정했는지 확인할 수 있도록
    # Question 모델과 Answer 모델에 수정일시를 modify_date 필드에 추가
    modify_date = models.DateTimeField(null=True, blank=True)
    # [21-12-15]  Question 모델 변경하기 一 다대다 관계(voter 추가)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

# 어떤 모델이 다른 모델(테이블)을 속성으로 가지면 Foreignkey를 이용
# on_delete는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미이다.

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    # [21-12-15] Answer 모델 변경하기 一 다대다 관계(voter 추가)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

