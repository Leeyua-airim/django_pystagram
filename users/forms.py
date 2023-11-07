'''
새롭게 생성한 py 파일
'''

from django import forms # django 내의 기존 클래스 상속

# 로그인 관련 정책
class LoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=4)