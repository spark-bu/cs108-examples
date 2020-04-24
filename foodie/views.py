from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse
from .models import Type, Recipe
from .forms import CreateRecipeForm, UpdateRecipeForm
# Create your views here.

def home(req):
    latest = Recipe.objects.order_by("-timestamp")[:6]
    context = {
        "latest": latest

    }
    return render(req, "index.html",context=context)

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'foodie/recipe_detail.html'
    context_object_name ='post'

class CreateRecipeView(CreateView):
    form_class = CreateRecipeForm
    model = Recipe
    template_name = 'foodie/create_recipe_form.html'
    context_object_name ='form'
    

class CreateCategoryView(CreateView):
    model = Type
    template_name = 'foodie/create_category_form.html'
    context_object_name ='form2'
    fields = ["name"]

class UpdateRecipeView(UpdateView):
    '''A view to create a new quote and save it to the database.'''
    form_class = UpdateRecipeForm
    template_name = "foodie/update_recipe_form.html"
    queryset = Recipe.objects.all()
