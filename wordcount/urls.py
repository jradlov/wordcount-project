
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home1'),     # path is what comes after http://127.0.0.1:8000/ (or netfield.com)
    path('count/', views.count, name='count1'),  # 'count1' = url 'count/' or whatever it is changed to
    path('about/', views.about, name='about1'),  # 'about1' = url 'about/'
]
