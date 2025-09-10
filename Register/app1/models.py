from django.db import models

# Create your models here.
class reigister(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone=models.IntergerField()
    pro_pic=models.ImageField(upload_to='user/')

    def __str__(self):
        return self.username

