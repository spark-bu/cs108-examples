from django import forms
from .models import Type, Recipe

class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name","image_of_food","category","recipe"]

class UpdateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name","image_of_food","category","recipe"]

    


