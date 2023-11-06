from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from config.views import index # 정의된 기능 호출

urlpatterns = [
    path('admin/', admin.site.urls),
    # users/ 로 접근하는 경우 users/urls.py 에 기반한 경로로 할당
    path('users/', include("users.urls")),
    # posts/ 로 접근하는 경우 posts/urls.py 에 기반한 경로로 할당
    path('posts/', include("posts.urls")),
    path("", index), # 경로가 없는경우 동작하는 함수
]

# 유저가 업로드한 정적파일을 제공한 URL 경로
# urls.py
# MEDIA_URL = "media/"
# MEDIA_ROOT = BASE_DIR / "media"
urlpatterns += static(
    prefix = settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT
)
