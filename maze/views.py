from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    game = [
        {'floor': 1, 'door': [1, 2, 3], 'success': 3},
        {'floor': 2, 'door': [4, 5, 6], 'success': 5},
        {'floor': 3, 'door': [7, 8, 9], 'success': 7}
    ]

    floor = int(request.GET.get('floor', 0))
    door = int(request.GET.get('door', 0))

    if floor == 0 and door == 0:  # 시작
        return render(request, 'maze/index.html', {'game': game[0]})
    elif door == 7:  # 탈출 성공
        return render(request, 'maze/end.html')
    elif door == int(game[floor - 1]['success']):  # 옳은 선택지
        return render(request, 'maze/index.html', {'game': game[floor]})
    else:  # 틀린 선택지
        return render(request, 'maze/gameover.html')
