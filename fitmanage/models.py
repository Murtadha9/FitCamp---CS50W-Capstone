
from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.




##############################################
class Type(models.Model):
    title=models.CharField(max_length=40)
    img=models.CharField(max_length=600,blank=True , null=True)
    price=models.FloatField(blank=True , null=True)
    type_details = models.TextField(blank=True , null=True)

    def __str__(self):
        return f"{self.title}"

##############################################
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100,blank=True , null=True)
    stars = models.FloatField()
    photo = models.ImageField(upload_to='trainers/')

    def __str__(self):
        return f"{self.name}"

##############################################

class AddMember(models.Model):
    img = models.ImageField(upload_to='members/', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    start= models.DateField()
    end= models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=400)
    type = models.ForeignKey(Type ,on_delete=models.CASCADE,blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    trainers = models.ForeignKey(Trainer ,on_delete=models.CASCADE,blank=True, null=True)
    payment_status = models.BooleanField(default=False)

    def is_expired(self):
        today = date.today()
        return today > self.end

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

##############################################


class WeeklyReport(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

