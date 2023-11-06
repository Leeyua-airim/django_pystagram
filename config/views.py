from django.shortcuts import render

# 기능 : index() 호출시 index.html 페이지 반환
def index(request):
    return render(request=request, template_name="index.html")
