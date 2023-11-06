from django.contrib.auth.models import AbstractUser


from django.db import models

# Django 내에 AbstractUser는 기본 유저형태를 가진 모델클래스
class User(AbstractUser):
    # 프로필 이미지
    profile_image = models.ImageField(
        verbose_name = "프로필 이미지",
        upload_to = "users/profile",
        # 업로드 될 경로: /Users/airim/github/django_pystagram/media/users/profile/
        blank=True, # 빈값 허용
    )
    # 프로필 소개
    short_description = models.TextField(
        verbose_name="소개글",
        blank=True
    )
