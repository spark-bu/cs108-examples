'''
Author: Soo Whan Park
Email: spark96@bu.edu
Filename: views.py
Description: Create views to display on the web page
'''
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
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
    ''' show the details for one recipe'''
    model = Recipe  #retrieve objects of type Recipe from the database
    template_name = 'foodie/recipe_detail.html' # name of the html file that links to the view
    context_object_name ='post' #how to find the data in the template file

class CreateRecipeView(CreateView):
    ''' create the new recipe '''
    form_class = CreateRecipeForm
    model = Recipe
    template_name = 'foodie/create_recipe_form.html'
    context_object_name ='form'
    

class CreateCategoryView(CreateView):
    ''' Create the new category of food'''
    model = Type
    template_name = 'foodie/create_category_form.html'
    context_object_name ='form2'
    fields = ["name"]
    success_url = reverse_lazy('home')

class UpdateRecipeView(UpdateView):
    ''' Update the existing recipes on database'''
    form_class = UpdateRecipeForm
    template_name = "foodie/update_recipe_form.html"
    queryset = Recipe.objects.all() # get all the objects from Recipe model

class DeleteRecipeView(DeleteView):
    ''' Delete the existing recipe post from the database'''
    model = Recipe
    template_name = 'foodie/delete_recipe_form.html'
    success_url = reverse_lazy('home') # back to homepage after deleteing the post

