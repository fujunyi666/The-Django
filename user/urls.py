from django.urls import path
from . import views
app_name='user'
urlpatterns=[
    path('login.html',views.loginView,name='login'),
    path('logout.html',views.logoutView,name='logout'),
    path('home/<int:page>.html',views.homeView,name='home')
]