from django.shortcuts import render, redirect

# 기능 : index() 호출시 index.html 페이지 반환
def index(request):
    if request.user.is_authenticated:
        return redirect('/posts/feeds/')
    else:
        return redirect('/users/login/')
    # return render(request=request, template_name="index.html")
