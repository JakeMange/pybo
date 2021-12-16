# [21-12-13] 템플릿 필터함수 사용
import markdown
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))