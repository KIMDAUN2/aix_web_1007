from django.shortcuts import render

def swrite(request):
    return render(request,'swrite.html')
#학생성적출력
def slist(request):
    return render(request,'slist.html')