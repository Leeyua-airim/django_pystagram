from django.urls import path
from users.views import login_view


urlpatterns = [
    # users/views.py
    # def login_view(request):
    #     return render(request=request,
    #                   template_name="user/login.html")
    path('login/', login_view), # login 으로 접근한 경우 다음 기능 호출
]
