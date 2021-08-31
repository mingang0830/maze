from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return render(request, "maze/game.html")
        else:
            return render(request, "maze/index.html", {'error_login':"없는 회원입니다."})
    else:
        return render(request, 'maze/index.html')


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
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, user)
            return render(request, 'maze/index.html')
        else:
            return render(request, 'maze/signup.html', {'error':"비밀번호가 일치하지 않습니다."})
    return render(request, 'maze/signup.html',)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('index')
    return render(request, 'maze/index.html')
