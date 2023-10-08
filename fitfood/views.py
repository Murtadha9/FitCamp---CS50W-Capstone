from django.shortcuts import get_object_or_404, render ,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User ,Recipe ,Category  ,NutritionInfo , Comment
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm ,CommentForm 
import random


############################################################
def indexfood(request):

    return render(request , 'food/indexfood.html')
############################################################
def homefood(request):
    

    search_form = RecipeSearchForm()
    recipe = None
    recipes = []
    message = ""  

    if 'search_query' in request.GET:
        search_query = request.GET['search_query']
        matching_recipes = Recipe.objects.filter(title__icontains=search_query)

        if matching_recipes.count() == 1:
            
            return redirect('recipe_detail', recipe_id=matching_recipes.first().id)
        elif matching_recipes.count() > 1:
            
            recipes = matching_recipes
        else:
            
            recipes = []
            message = f"No recipes found matching '{search_query}'."


    recipes = Recipe.objects.all()
    return render(request, 'food/homefood.html', {'recipe': recipe, 'recipes': recipes, 'search_form': search_form, 'message': message})
############################################################

def category(request, id):
    category = Category.objects.get(pk=id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'food/category.html', {'category': category, 'recipes': recipes})
############################################################

def vegan(request):
    recipes = Recipe.objects.filter(category__name='Vegan')
    return render(request, 'food/vegan.html', {'recipes': recipes})

############################################################

def vegetarian(request):
    recipes = Recipe.objects.filter(category__name='Vegetarian')
    return render(request, 'food/vegetarian.html', {'recipes': recipes})

############################################################

def sweet(request):
    recipes = Recipe.objects.filter(category__name='Sweet Diet')
    return render(request, 'food/sweet.html', {'recipes': recipes})

def high_protein(request):
    recipes = Recipe.objects.filter(category__name='High Protein')
    return render(request, 'food/high_protein.html', {'recipes': recipes})

def seafood(request):
    recipes = Recipe.objects.filter(category__name='Sea Food')
    return render(request, 'food/seafood.html', {'recipes': recipes})

############################################################

def salad(request):
    recipes = Recipe.objects.filter(category__name='Salad')
    return render(request, 'food/salad.html', {'recipes': recipes  })

############################################################

def low_carbs(request):
    recipes = Recipe.objects.filter(category__name='Low Carbs')
    return render(request, 'food/low_carbs.html', {'recipes': recipes})

############################################################

def pasta(request):
    recipes = Recipe.objects.filter(category__name='Pasta')
    return render(request, 'food/pasta.html', {'recipes': recipes})

############################################################
def recommended(request):
    all_recipes = Recipe.objects.all()

    
    num_recommendations = 5  

    
    if num_recommendations > len(all_recipes):
        recommended_recipes = all_recipes
    else:
        recommended_recipes = random.sample(list(all_recipes), num_recommendations)

    return render(request, 'food/recommended.html', {'recommended_recipes': recommended_recipes})




############################################################

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    nutritions = NutritionInfo.objects.get(recipe=recipe)
    
    comments = recipe.comments.all() 

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user  
            new_comment.recipe = recipe 
            new_comment.save()
            return redirect('recipe_detail', recipe_id=recipe_id)

    else:
        comment_form = CommentForm()


    return render(request, 'food/recipe_detail.html', {'recipe': recipe, 
                                                        'nutritions':nutritions ,
                                                        'comments': comments,
                                                        'comment_form': comment_form })




############################################################

def loginfood(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("homefood"))
        else:
            return render(request, "food/loginfood.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "food/loginfood.html")


def logoutfood(request):
    logout(request)
    return HttpResponseRedirect(reverse("indexfood"))


def registerfood(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "food/registerfood.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "food/registerfood.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("homefood"))
    else:
        return render(request, "food/registerfood.html")

