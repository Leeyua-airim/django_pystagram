from django.urls import path
from users.views import login_view, logout_view, signup


urlpatterns = [
    # users/views.py
    # def login_view(request):
    #     return render(request=request,
    #                   template_name="user/login.html")
    path('login/', login_view), # login 으로 접근한 경우 다음 기능 호출
    path('logout/', logout_view), # logout 으로 접근하는 경우 다음 함수 실행
    path('signup/', signup)
]
