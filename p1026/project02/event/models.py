from django.db import models
from member.models import Member

class Event(models.Model):
    eno = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.SET_NULL,blank=True,null=True)
    etitle = models.CharField(max_length=1000)
    econtent = models.TextField()    
    ehit = models.IntegerField(default=1)
    first_date = models.DateTimeField(auto_now=True,blank=True)  #이벤트 시작일
    end_date = models.DateTimeField(auto_now=True,blank=True)    #이벤트 마지막일
    edate = models.DateTimeField(auto_now=True,blank=True)       #등록일
    efile = models.ImageField(blank=True,upload_to='event') 
    efile2 = models.ImageField(blank=True,upload_to='event') 

    def __str__(self):
        return f'{self.eno},{self.etitle},{self.edate}'


