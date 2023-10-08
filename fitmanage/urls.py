from django.urls import path
from . import views


urlpatterns=[
    path("", views.indexmanage, name="indexmanage"),
    path("loginmanage", views.loginmanage, name="loginmanage"),
    path("logoutmanage", views.logoutmanage, name="logoutmanage"),
    path("registermanage", views.registermanage, name="registermanage"),

    ###########################################################

    path("displayMember", views.displayMember, name="displayMember"),
    path("addMember", views.add_Member, name="addMember"),
    path("trainers", views.trainers, name="trainers"),

    path("report", views.report, name="report"),
    path("convertToExcel", views.convertToExcel, name="convertToExcel"),

    path("membership", views.membership, name="membership"),
    

]