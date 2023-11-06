from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# users/models.py
# class User(AbstractUser):
#     pass
from users.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {'fields' : ("username", "password")}),
        ("개인정보", {"fields" : ("first_name", "last_name", "email")}),
        # 여기서는 users/models.py 에 User 클래스의 객체를 활용
        ("추가필드", {"fields" : ("profile_image", "short_description")}),
        # is_active, is_staff, is_superuser 는
        # AbstractUser 를 상속받으면 자동으로 생성되는 필드
        ("권한", {"fields" : ("is_active", "is_staff", "is_superuser")}),
        ("중요한 일정", {"fields" : ("last_login", "date_joined")}),
    ]

