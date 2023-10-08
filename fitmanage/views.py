from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,redirect ,get_object_or_404
from django.urls import reverse
from .models import User ,Trainer
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import AddMember , WeeklyReport ,Type
from .forms import memberForm ,WeeklyReportForm
import pandas as pd


# Create your views here.


def indexmanage(request):
    return render(request , 'manage/indexmanage.html')


######################################################

def displayMember(request):
    allMembers=AddMember.objects.all().order_by('id')


    query = request.GET.get('q')
    if query:
        allMembers = allMembers.filter(first_name__icontains=query) | allMembers.filter(last_name__icontains=query)



    return render(request,'manage/allMembers.html' , {'allMembers':allMembers})




######################################################
def trainers(request):
    trainers = Trainer.objects.all()
    
    return render(request, 'manage/trainers.html', {'trainers': trainers})

######################################################
"""
def add_Member(request):
    if request.method == 'POST':
        form = memberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('displayMember')  # Redirect to the page that displays all players
    else:
        form = memberForm()
    return render(request, 'manage/addMember.html', {'form': form})
"""

def add_Member(request):

    trainers=Trainer.objects.all()
    types=Type.objects.all()

    if request.method == 'POST':

        img = request.FILES.get('img')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        start = request.POST.get('start')
        end = request.POST.get('end')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        type_id = request.POST.get('type')
        amount = request.POST.get('amount')
        trainers_id = request.POST.get('trainers')
        payment_status = request.POST.get('payment_status') == 'on'  

        
        member = AddMember(
            img=img,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            start=start,
            end=end,
            phone_number=phone_number,
            address=address,
            type_id=type_id,
            amount=amount,
            trainers_id=trainers_id,
            payment_status=payment_status
        )
        member.save()

        return redirect('displayMember')  
    else:
        return render(request, 'manage/addMember.html' ,{'trainers':trainers ,'types':types})




######################################################
def report(request):
    if request.method == 'POST':
        form = WeeklyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report')

    else:
        form = WeeklyReportForm()

    reports = WeeklyReport.objects.all()

    context = {
        'form': form,
        'reports': reports,
    }

    return render(request, 'manage/reports.html', context)

######################################################
def convertToExcel(request):
    reports = WeeklyReport.objects.all()
    data = {'Title': [report.title for report in reports],
            'Content': [report.content for report in reports],
            'Created At': [report.created_at.strftime('%Y-%m-%d %H:%M:%S') for report in reports]}

    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="weekly_reports.xlsx"'
    df.to_excel(response, index=False)

    return response
######################################################


def membership(request):
    memberships=Type.objects.all()
    return render(request , 'manage/membership.html' ,{'memberships':memberships})




######################################################


def loginmanage(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("membership"))
        else:
            return render(request, "manage/loginmanage.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "manage/loginmanage.html")


def logoutmanage(request):
    logout(request)
    return HttpResponseRedirect(reverse("indexmanage"))


def registermanage(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "manage/registermanage.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "manage/registermanage.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("membership"))
    else:
        return render(request, "manage/registermanage.html")

