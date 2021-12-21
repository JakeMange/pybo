from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# [21-12-14] 회원 가입을 위한 signup 함수 정의
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # 회원가입 후 자동 로그인
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})
