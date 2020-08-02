from django.shortcuts import render
from django.db.models import Avg

# Create your views here.
from .models import T1

def book_short(request):
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    star_avg = f"{T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f}"

    # 获取大于3星的评论数
    queryset = T1.objects.values('n_star')
    condtions = {'n_star__gt': 3}
    plus = queryset.filter(**condtions)
    plus_data = plus.values()
    plus_count = plus.count()

    # 获取小于等于3星的评论数
    queryset = T1.objects.values('n_star')
    condtions = {'n_star__lte': 3}
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())

def short_tables(request):
    # 获取所有评论
    shorts = T1.objects.all()

    return render(request, 'table.html', locals())
