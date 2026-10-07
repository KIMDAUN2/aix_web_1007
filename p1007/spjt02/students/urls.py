from django.urls import path,include
from . import views    #자기폴더는 . 으로 가능

urlpatterns = [
    path('s_write/',views.s_write),  #students app안에 urls를 찾아감
]