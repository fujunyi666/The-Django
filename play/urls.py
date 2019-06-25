from django.urls import path
from . import views
app_name='play'
urlpatterns=[
    path('<int:song_id>.html',views.playView,name='play'),
    path('download/<int:song_id>.html',views.downloadView,name='download')
]