from django.shortcuts import render
from member.models import Member


def logout(request):
    #섹션 모두 삭제
    request.session.clear()
    context ={'temp':2}
    return render(request,'login.html',context)

#GET-로그인페이지, POST-로그인확인
def login(request):
    if request.method =='GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        id= request.POST.get('id')
        pw= request.POST.get('pw')
        qs = Member.objects.filter(id=id,pw=pw).first()
        if qs:
            request.session['session_id']=id
            request.session['session_nickname']=qs.nickname
            context ={'temp':1}
        else:
            context ={'temp':0}
        print(f'데이터확인: {id},{pw},{context},{qs}')
        return render(request, 'login.html',context)
