from django.contrib import admin

from .models import  WorkoutCategory, Exercise ,Fitness ,UserQuery




admin.site.register(WorkoutCategory)
admin.site.register(Exercise)
admin.site.register(Fitness)
admin.site.register(UserQuery)


