from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    c_name=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    date=models.DateField(auto_now=True,auto_now_add=False)
    director=models.CharField(max_length=100,null=True)

# from django.db import models

# class Company(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     director = models.CharField(max_length=50)

    def __str__(self):
        return self.name