from django.shortcuts import render,redirect
from django.http import HttpResponse # 不找模板直接輸出
import random,datetime
from mysite import models

def date(request):
    now = datetime.datetime.now()
    # return HttpResponse(now)
    return HttpResponse('<h1 style="font-family:微軟正黑體;">現在時刻:{}<h1><hr>'.format(now))

def lotto(request):
    numbers = [n for n in range(1,43)]
    random.shuffle(numbers) # 打亂numbers
    lotto = numbers[:6]
    special = numbers[6]
    '''
    special = random.randint(1,42)
    lotto = [random.randint(1,42) for i in range(6)]
    '''
    return render(request,'lotto.html',locals())

def play(request,id):
    try:
        post = models.Post.objects.get(id = int(id))
        return render(request,'play.html',locals())
    except:
        return redirect('/')

def index(request):
    posts = models.Post.objects.all()
    return render(request,'index.html',locals())
    #render(request,'index.html',locals()) => 渲染(,,所有)
