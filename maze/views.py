from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


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
    game = [
        {'floor': 0, 'door': [1, 2, 3], 'success': 3},
        {'floor': 1, 'door': [4, 5, 6], 'success': 5},
        {'floor': 2, 'door': [7, 8, 9], 'success': 7}
    ]

    current_floor = int(request.GET.get('floor', 0))
    next_floor = current_floor + 1
    door = int(request.GET.get('door', 0))

    if current_floor == 0 and door == 0:  # 시작
        return render(request, 'maze/game.html', {'game': game[0]})
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
                    username=username, password=password1
                )
                user.save()
            return redirect('login')
        except:
            return render(request, 'maze/signup.html', {'error': "이미 가입된 회원입니다."})
    return render(request, 'maze/signup.html',)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('login')
    return render(request, 'maze/login.html')
