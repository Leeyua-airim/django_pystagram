from django.shortcuts import render, redirect

# 기능 : 호출시 html 랜딩
# 기능 : 로그인 여부에 따라 동작을 구분하기 위해 요청을 보낸 사용자의 정보가 필요
def feeds(request):
    # 만약 로그인을 하지 않은경우
    if not request.user.is_authenticated:
        # users/login 으로 이동
        return redirect('/users/login/')

    # user = request.user # 요청으로 부터 사용자의 정보를 가져온다.
    # print("user : ", user)
    # # user :  AnonymousUser (익명 사용자/로그인하지 않은경우)
    # # 가져온 사용자가 '로그인 했는지' 여부를 가져온다.
    # # user :  admin (로그인한 경우)

    # is_authenticated = user.is_authenticated
    # print("is_authenticated : ", is_authenticated)
    # # is_authenticated :  False
    # # is_authenticated :  True

    return render(request=request,
                  template_name="posts/feeds.html")



