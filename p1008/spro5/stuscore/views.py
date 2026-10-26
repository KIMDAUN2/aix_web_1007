from django.shortcuts import render,redirect
from stuscore.models import Student

def score_write(request):
    if request.method == 'GET':
        print('GET 페이지가 로딩되었습니다.')
        return render(request,'score_write.html')
    elif request.method == 'POST':
        print('POST 페이지가 로딩되었습니다.')
        no= request.POST.get('no')
        name= request.POST.get('name')
        school= request.POST.get('school')
        major= request.POST.get('major')
        grade= request.POST.get('grade')
        stature= request.POST.get('stature')
        kor= request.POST.get('kor')
        eng= request.POST.get('eng')
        math= request.POST.get('math')
        sw= request.POST.get('sw')
        #qs= Stu(name='홍길동, major='국문학과', grade=1, age=20,gender='남자')
        qs= Student(no=no,name=name,school=school,major=major,grade=grade,stature=stature,kor=kor,eng=eng,math=math,sw=sw)
        qs.save()

        print(no,name,school,major,grade,stature,kor,eng,math,sw)
        return redirect('/')