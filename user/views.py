from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect

from index.models import Dynamic
from user.models import *
from django.db.models import Q
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from .form import MyUserCreationForm

def loginView(request):
    user=MyUserCreationForm()
    if request.method=="POST":
        if request.POST.get('loginUser',''):
            loginUser=request.POST.get('loginUser','')
            password=request.POST.get('password','')
            if MyUser.objects.filter(Q(mobile=loginUser)|Q(username=loginUser)):
                user=MyUser.objects.filter(Q(mobile=loginUser)|Q(username=loginUser)).first()
                if check_password(password,user.password):
                    login(request,user)
                    return redirect('user/home/1.html')
                else:
                    tips='密码错误'
            else:
                tips='用户不存在'
        else:
            user=MyUserCreationForm(request.POST)
            if user.is_valid():
                user.save()
                tips='注册成功'

            else:
                if user.errors.get('username',''):
                    tips=user.errors.get('username','注册失败')
                else:
                    tips=user.errors.get('mobile','注册失败')
    return render(request,'login.html',locals())

def logoutView(request):
    logout(request)
    return  redirect('/')

@login_required(login_url='/user/login.html')
def homeView(request, page):
    # 热搜歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    # 分页功能
    song_info = request.session.get('play_list', [])
    paginator = Paginator(song_info, 3)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', locals())

# 自定义404和500的错误页面
def page_not_found(request):
    return render(request, 'error404.html', status=404)


