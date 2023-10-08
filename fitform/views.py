from django.http import HttpResponseRedirect
from django.shortcuts import render ,get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User,WorkoutCategory,  Exercise , Fitness
from django.contrib.auth.decorators import login_required
from .forms import UserQueryForm





def indexform(request):
    return render(request ,'form/indexform.html')

###############################################################################

def homeform(request):
    categories = WorkoutCategory.objects.all()
    fitness_items = Fitness.objects.all()
    return render(request ,'form/homeform.html',{'categories': categories ,'fitness_items':fitness_items})

###############################################################################

def body(request):
    categories = WorkoutCategory.objects.all()
    return render(request, 'form/body.html', {'categories': categories})

###############################################################################

def category_exercises(request, category_id):
    category = WorkoutCategory.objects.get(pk=category_id)
    exercises = Exercise.objects.filter(category=category)
    return render(request, 'form/category_exercises.html', {'category': category, 'exercises': exercises})

###############################################################################

def search(request):
    query = request.GET.get('query', '')
    exercises = Exercise.objects.filter(name__icontains=query)
    
    return render(request, 'form/search_results.html', {'query': query, 'exercises': exercises})

###############################################################################

def fitness(request):
    fitness_items = Fitness.objects.all()
    return render(request, 'form/fitness.html', {'fitness_items': fitness_items})

###############################################################################

def search_fitness(request):
    query = request.GET.get('query')
    fitness_items = Fitness.objects.filter(title__icontains=query)
    return render(request, 'form/search_fitness.html', {'fitness_items': fitness_items, 'query': query})
###############################################################################

def fitness_details(request, fitness_id):
    fitness_item = get_object_or_404(Fitness, pk=fitness_id)
    return render(request, 'form/fitness_details.html', {'fitness_item': fitness_item})
###############################################################################
def help(request):
    if request.method == 'POST':
        form = UserQueryForm(request.POST)
        if form.is_valid():
            
            query = form.save(commit=False)
            query.user = request.user  
            query.save()
            return redirect('recived')

    else:
        form = UserQueryForm()

    return render(request, 'form/helpform.html', {'form': form})


def recived(request):
    return render(request , 'form/recivedform.html')



###############################################################################
def loginform(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("homeform"))
        else:
            return render(request, "form/loginform.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "form/loginform.html")


def logoutform(request):
    logout(request)
    return HttpResponseRedirect(reverse("indexform"))


def registerform(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "form/registerform.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "form/registerform.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("homeform"))
    else:
        return render(request, "form/registerform.html")
