from django.db import models

# Create your models here.


class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    pay = models.IntegerField()
    pub_date = models.DateTimeField()
    body = models.TextField()
    number = models.IntegerField(default=0)

# blog에서 object가 아닌 타이틀 명으로 보여지게 하는 것
    def __str__(self):
        return self.title
