from django.urls import path
from . import views
app_name='comment'
urlpatterns=[
    path('<int:song_id>.html',views.commentView,name='comment')
]