'''
Author: Soo Whan Park
Email: spark96@bu.edu
Filename: urls.py
Description: map the url to the view. Each post record is represented as <int:pk>
'''
from django.urls import path
from foodie import views #import all the views

# Urls for all views
urlpatterns = [
    # map the URL to the view
    path('', views.home, name = 'home'), # generic class-based view
    path('post/<int:pk>', views.RecipeDetailView.as_view(), name = 'post'), #show one recipe
    path('post/create', views.CreateRecipeView.as_view(), name = 'create_post'), #create the post
    path('post/<int:pk>/update', views.UpdateRecipeView.as_view(), name = 'update'), #update the post
    path('post/<int:pk>/delete', views.DeleteRecipeView.as_view(), name = 'delete'), #delete the post
    path('post/add', views.CreateCategoryView.as_view(), name = 'create_category'), # create the category
    
]