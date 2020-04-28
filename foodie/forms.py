from django import forms
from .models import Type, Recipe

class CreateRecipeForm(forms.ModelForm):
    ''' Form that provides necessary fields for creating the new recipe in the view'''
    class Meta:
        model = Recipe
        fields = ["name","image_of_food","category","recipe"]

class UpdateRecipeForm(forms.ModelForm):
    ''' Form that provides necessary fields for updating the recipe in the view'''
    class Meta:
        model = Recipe
        fields = ["name","image_of_food","category","recipe"]

    


