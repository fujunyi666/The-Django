from django.shortcuts import render
from index.models import *

def rankingView(request):
    search_song=Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    All_list=Song.objects.values('song_type').distinct()
    song_type=request.GET.get('type','')
    if song_type:
        song_info=Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by('-dynamic_plays').all()[:10]

    else:
        song_info=Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
    return  render(request,'ranking.html',locals())

# 自定义404和500的错误页面
def page_not_found(request):
    return render(request, 'error404.html', status=404)