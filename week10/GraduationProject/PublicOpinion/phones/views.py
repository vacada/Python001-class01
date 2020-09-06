from django.shortcuts import render
from django.db.models import Avg

# Create your views here.
from .models import Comments


def phone_comment(request, rank=1):
    if rank == None:
        phone_rank = 1
    phone_rank = rank
    # 排名
    phone_rank = phone_rank

    # 评论数量
    comment_num = Comments.objects.filter(phone_rank=phone_rank).count()

    # 平均情感值
    analysis_avg = f"{Comments.objects.filter(phone_rank=phone_rank).aggregate(Avg('comment_analysis'))['comment_analysis__avg']:0.3f}"
    
    # 录入时间
    # input_time = f"{Comments.objects.filter(phone_rank=1).values('input_time').}"

    # 大于0.5的评论数
    queryset = Comments.objects.filter(phone_rank=phone_rank).values('comment_analysis')
    condtions = {'comment_analysis__gt': 0.5}
    plus = queryset.filter(**condtions).count()

    # 小于0.5的评论数
    queryset = Comments.objects.filter(phone_rank=phone_rank).values('comment_analysis')
    condtions = {'comment_analysis__lte': 0.5}
    minus = queryset.filter(**condtions).count()

    # 获取排行榜
    ranks = Comments.objects.values('phone_rank', 'phone_name').distinct().order_by('phone_rank')

    return render(request, 'result.html', locals())

def phone_rank(request):
    phone_comments = Comments.objects.all()
    return render(request, 'table.html', locals())
