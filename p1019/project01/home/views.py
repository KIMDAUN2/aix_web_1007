from django.shortcuts import render
from . import views

app_name='home'
def index(request):
    return render(request, 'index.html')
