from django.db import models
from django.contrib.auth.models import User

# Create your models here.



#########################################

class WorkoutCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images' , null=True , blank=True)


    def __str__(self):
        return f'{self.name}'
#########################################
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(WorkoutCategory, on_delete=models.CASCADE , null=True , blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='exercise_images',null=True , blank=True)

    def __str__(self):
        return f'{self.name}'
#########################################


class Fitness(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='exercise_images',null=True , blank=True)
    description = models.TextField()
    def __str__(self):
        return f'{self.title}'


#########################################
class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.user}"
