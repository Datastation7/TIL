from django.shortcuts import render
from django.http.response import HttpResponse
import random
# Create your views here.

def hello_world(request):
    # 응답으로 HTML을 렌더링하겠다.
    # django => 무조건 HTML 파일은 폴더명 templates/ 에서 찾는다.
    return render(request, 'hello_world.html')

def lunch(request):
    menus = ['짜장', '보쌈', '삼겹살', '치킨', '샐러드', '굶기']
    menu = random.choice(menus)
    context = {
        'menu' : menu,
    }
    return render(request, 'lunch.html', context)

def lotto(request):
    lucky = random.sample(range(1, 46), 6)
    lucky.sort()
    context = {
        'lucky' : lucky,
        'is_jackpot' : True,
    }
    return render(request, 'lotto.html', context)
