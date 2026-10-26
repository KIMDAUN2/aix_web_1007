from django.shortcuts import render,redirect
from students.models import Students


# 학생상세보기
def sview(request,name):
    print(f'name 데이터 : {name}')
    qs = Students.objects.get(name=name) #1개의 정보전송
    context = {'stu':qs}
    return render(request, 'sview.html',context)


def swrite(request):
    if request.method == 'GET':
        return render(request, 'swrite.html')
    elif request.method == 'POST':
        name = request.POST.get('name') #데이터가 없어도 에러가 나지 않음
        major = request.POST.get('major')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        gender = request.POST.get('gender')
        qs = Students(name=name,major=major,age=age,grade=grade,gender=gender)
        qs.save()
        print(f'확인 : {name},{major}')

        return redirect('/students/slist')



def slist(request):
    qs = Students.objects.all()
    context = {'list':qs}
    return render(request,'slist.html',context)
