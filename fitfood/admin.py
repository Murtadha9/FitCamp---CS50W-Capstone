from django.contrib import admin

from .models import Recipe , Category ,Ingredient , NutritionInfo ,Comment


#admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(NutritionInfo)
admin.site.register(Comment)

