from django.shortcuts import render

# 기능 : 호출시 html 랜딩
def feeds(request):
    return render(request=request,
                  template_name="posts/feeds.html")