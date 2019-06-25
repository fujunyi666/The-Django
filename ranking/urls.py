from django.urls import path
from . import views
app_name='ranking'
urlpatterns=[
    path('',views.rankingView,name='ranking')
]