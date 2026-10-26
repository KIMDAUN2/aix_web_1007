from django.db import models

class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    major=models.CharField(max_length=100)
    grade=models.IntegerField(default=0)
    stature=models.FloatField(default=0)
    kor=models.IntegerField(default=0)
    eng=models.IntegerField(default=0)
    math=models.IntegerField(default=0)
    sw=models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.no},{self.name},{self.school},{self.major},{self.grade},{self.stature},{self.kor},{self.eng},{self.math},{self.sw}'