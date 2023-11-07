from django.shortcuts import render, redirect
from users.forms import LoginForm
def login_view(request):
    # 만약 로그인이 되어 있다면
    if request.user.is_authenticated:
        # 다음
        return redirect('/posts/feeds/')

    # 로그인이 되어 있지 않은경우
    # 로그인 관련 정책 클래스 호출 후 이를 랜더링 페이지로 넘긴다.
    form = LoginForm()
    context = {
        'form' : form
    }
    return render(request=request,
                  template_name="users/login.html",
                  context=context)