from django.contrib import admin

from .models import AddMember , User , Trainer,Type ,WeeklyReport

admin.site.register(AddMember)
#admin.site.register(User)
admin.site.register(Type)
admin.site.register(Trainer)
admin.site.register(WeeklyReport)


