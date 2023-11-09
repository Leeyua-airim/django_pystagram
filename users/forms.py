'''
새롭게 생성한 py 파일
'''
from django import forms # django 내의 기존 클래스 상속

# 로그인 관련 정책
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={"placeholder":"사용자명 (3자리 이상)"}
        ),
    )
    password = forms.CharField(min_length=4,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder':"비밀번호(4자리 이상)"}
                               ))


# 회원가입시 받을 값
class SignupForm(forms.Form):
    # 사용자 이름값
    username = forms.CharField()
    # 패스워드
    password1 = forms.CharField(widget=forms.PasswordInput)
    # 패스워드 확인 값
    password2 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()
