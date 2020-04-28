'''
Author: Soo Whan Park
Email: spark96@bu.edu
Filename: models.py
Description: this defines the models of projects
'''
from django.db import models
from django.urls import reverse

# Create your models here.

class Type(models.Model):
    '''Encapsulate the category of a food ex)American, Italian, Korean, Japanese...'''
    name = models.CharField(max_length=100) # Categorize the food 
    
    #String representation
    def __str__(self):
        return self.name

class Recipe(models.Model):
    ''' Encapsulate the recipe of a food. Post the recipe of food with 
    its name, image, category from Type class and the recipe'''
    # data attributes of a recipe
    name = models.CharField(max_length=100)
    image_of_food = models.ImageField(blank = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey('Type', on_delete="CASCADE")
    recipe = models.TextField(blank=True)

    #String representation
    def __str__(self):
        return self.name
    #keeps track of each posts. Ex) First post -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])


