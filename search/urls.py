from django.urls import path
from . import views
app_name='search'
urlpatterns=[
    path('<int:page>.html',views.searchView,name='search'),
]