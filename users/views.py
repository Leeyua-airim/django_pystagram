from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm,SignupForm
from users.models import User

def login_view(request):
    # 만약 로그인이 되어 있다면
    if request.user.is_authenticated:
        # 다음
        return redirect('/posts/feeds/')

    # 로그인이 되어있지 않은 경우
    # 만약 POST 인 경우
    if request.method == 'POST':
        # 로그인을 시도하는 경우
        print("[안내] if request.method == 'POST': 동작")
        form = LoginForm(data=request.POST)

        # 해당 값이 있는 경우
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # 확인
            user = authenticate(username=username,
                                password=password)

            # 로그인 여부 판단
            if user:
                print("로그인 성공 ~ ")
                # Django 가 제공하는 login() 함수
                login(request, user)
                return redirect('/posts/feeds/')

            else:
                # print("로그인에 실패하였습니다. ㅋ")
                form.add_error(None,
                               "입력한 자격증명에 해당하는 사용자가 없습니다.")



        context = {'form' : form}
        return render(request=request,
                      template_name="users/login.html",
                      context=context)
    # get 인 경우
    else:
        form = LoginForm()
        context = {'form' : form}
        return render(request,
                      'users/login.html',
                      context)


# 로그아웃에 활용되는 함수
def logout_view(request):
    # 해당 함수가 동작하면 로그아웃기능 수행
    logout(request)

    # 로그인 페이지 리다이렉트
    return redirect("/users/login/")

# 회원가입 기능
def signup(request):
    # 회원가입을 위해 POST 요청을 보낸경우
    if request.method == "POST":
        # 입력받은 값을 form 변수에 저장
        form = SignupForm(data=request.POST, files=request.FILES)

        # 값이 있는 경우 TRUE 반환
        if form.is_valid():
            # 각각의 값을 변수에 할당
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            profile_image = form.cleaned_data['profile_image']
            short_description = form.cleaned_data['short_description']

            # 비밀번호와 비밀번호 확인이 같은지 검사
            if password1 != password2:
                form.add_error("password2","비밀번호와 비밀번호 확인란의 값이 다릅니다.")

            # exits()는 이미 존재하는 값을 확인
            if User.objects.filter(username=username).exists():
                form.add_error("username", "입력한 사용자명은 이미 사용중입니다.")

            # 만약
            if form.errors:
                context={'form':form}
                return render(request, "users/signup.html", context)

            # 에러가 없다면 유저 생성
            else:
                user = User.objects.create_user(
                    username = username,
                    password=password1,
                    profile_image = profile_image,
                    short_description = short_description,
                )
                login(request, user)
                # /posts/feeds/ 라 하면 저 경로 그대로 감
                # posts/feeds/면 이전 경로에 이어서 들어감
                return redirect("/posts/feeds/")


        context = {'form' : form}
        print("여기 동작")
        return render(request, 'users/signup.html',context)

    else:
        # 회원가입하러 온 경우 / get 인 경우
        print("여긴?")
        form = SignupForm()
        # print("[form]", form)
        # 회원가입을 위한 폼 전달
        context = {"form" : form}
        return render(request=request,
                      template_name='users/signup.html',
                      context=context)