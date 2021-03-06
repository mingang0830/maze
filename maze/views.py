from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Now


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            login(request, user)
            return redirect('game')
        else:
            return render(request, "maze/login.html", {'error_login': "정확한 정보를 입력해주세요."})
    else:
        return render(request, 'maze/login.html')


def game(request):
    if request.user.id is None:
        return redirect('login')

    game = [
        {'floor': 0, 'door': [1, 2, 3], 'success': 3},
        {'floor': 1, 'door': [4, 5, 6], 'success': 5},
        {'floor': 2, 'door': [7, 8, 9], 'success': 7}
    ]

    current_floor = int(request.GET.get('floor', 0))
    next_floor = current_floor + 1
    door = int(request.GET.get('door', 0))
    qset = Now.objects.all()

    if qset.filter(u_id=request.user.id):  # now 테이블에 값이 있는지 조회
        now_info = qset.get(u_id=request.user.id)
        saved_floor = now_info.now_floor
    else:
        saved_floor = 0

    if current_floor == 0 and door == 0:  # 시작
        return render(request, 'maze/game.html', {'game': game[saved_floor]})
    elif door == 7:  # 탈출 성공
        return render(request, 'maze/end.html')
    elif door == int(game[current_floor]['success']):  # 옳은 선택지
        return render(request, 'maze/game.html', {'game': game[next_floor]})
    else:  # 틀린 선택지
        return render(request, 'maze/gameover.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        try:
            if username == '':
                return render(request, 'maze/signup.html', {'error': "Username을 입력해주세요."})
            elif password1 == '':
                return render(request, 'maze/signup.html', {'error': "비밀번호 입력해주세요."})
            elif password1 != password2:
                return render(request, 'maze/signup.html', {'error': "비밀번호가 일치하지 않습니다."})
            else:
                user = User.objects.create_user(
                    username=username, password=password1성
                )
                user.save()
            return redirect('login')
        except:
            return render(request, 'maze/signup.html', {'error': "이미 가입된 회원입니다."})
    return render(request, 'maze/signup.html',)


def logout(request):
    auth.logout(request)
    return redirect('login')


def save(request):
    if request.method == 'POST':
        now_floor = request.POST.get('now_floor')
        u_id = request.user.id  # signin user 선언을 request로 가져옴
        queryset = Now.objects.all()  # SELECT * FROM now
        now_u_id = queryset.filter(u_id=u_id)  # 데이터 조회
        if now_u_id:
            now_u_id.update(now_floor=now_floor)
        else:
            Now(now_floor=now_floor, u_id=u_id).save()
        return redirect('game')




