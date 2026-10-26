from django.shortcuts import render,redirect
from member.models import Member
#-------------------------------------------------------
#회원수정페이지: GET 회원수정: POST
def mupdate(request,id):
    if request.method == 'GET':
        print(f"확인데이터 :{id} ")
        qs= Member.objects.get(id=id)
        tel= qs.tel.split('-')   #010-0000-0000 -> [010,0000,0000]
        context = {'member':qs,'tel':tel}
        return render(request,'mupdate.html',context)
    elif request.method =='POST':
        # id =request.session.session_id
        pw =request.POST.get('pw')
        name=request.POST.get('name')
        nickname =request.POST.get('nickname')
        tel1 =request.POST.get('tel1')
        tel2 =request.POST.get('tel2')
        tel3 =request.POST.get('tel3')
        tel =f'{tel1}-{tel2}-{tel3}'
        gender =request.POST.get('gender')
        hobby =request.POST.getlist('hobby')

        #id검색
        qs = Member.objects.get(id=id)
        qs.name= name
        qs.pw=pw
        qs.nickname=nickname
        qs.tel=tel
        qs.gender=gender
        qs.hobby=hobby
        qs.save()
        #db저장
        #Member(id=id,pw=pw,nickname=nickname,tel=tel,gender=gender,hobby=hobby).save()
        print(f'{id},{pw},{nickname},{tel},{gender},{hobby},{name}')
        return redirect('/')

#--------------------------------------------------------
#회원가입페이지 : GET, 회원가입추가: POST
def mwrite(request):
    if request.method == 'GET':
        return render(request,'mwrite.html')
    elif request.method =='POST':
        id =request.POST.get('id')
        pw =request.POST.get('pw')
        name=request.POST.get('name')
        nickname =request.POST.get('nickname')
        tel1 =request.POST.get('tel1')
        tel2 =request.POST.get('tel2')
        tel3 =request.POST.get('tel3')
        tel =f'{tel1}-{tel2}-{tel3}'
        gender =request.POST.get('gender')
        hobby =request.POST.get('hobby')

        #db저장
        #Member(id=id,pw=pw,nickname=nickname,tel=tel,gender=gender,hobby=hobby).save()
        Member.objects.create(id=id,pw=pw,nickname=nickname,tel=tel,gender=gender,hobby=hobby,name=name)
        print(f'{id},{pw},{nickname},{tel},{gender},{hobby},{name}')
        return render(request,'mresult.html')



#---------------------------------------------------------
#로그아웃
def logout(request):
    context = {'temp':2}
    #섹션 모두 종료
    request.session.clear()
    return render(request,'login.html',context)



#로그인페이지:GET,로그인확인:post
def login(request):
    if request.method == 'GET':
        #쿠키검색
        cook_id= request.COOKIES.get('cook_id','') #없으면 ''
        if cook_id:
            context = {'cook_id':cook_id}
        else:
            context ={}
        return render(request,'login.html',context)
    
    elif request.method == 'POST':
        id =request.POST.get('id')
        pw =request.POST.get('pw')
        rememberId =request.POST.get('rememberId')
        #db확인
        qs = Member.objects.filter(id=id,pw=pw).first() #filter rjator -> 여러개
        if qs: #로그인성공
            context ={'temp':1}
            #session추가
            request.session['session_id']=qs.id
            request.session['session_nickname']=qs.nickname

        else:  #로그인실패
            context ={'temp':0}

        print(f'데이터확인 : {id},{pw},{rememberId},{context}')
        response = render(request,'login.html',context)
        #쿠키적용
        if rememberId:
            #쿠키설정
            response.set_cookie('cook_id',id,max_age=60*60*24*365)
        else:
            #쿠키삭제
            response.delete_cookie('cook_id')
        return response