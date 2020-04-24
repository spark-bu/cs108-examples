from django.urls import path
from foodie import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('post/<int:pk>', views.RecipeDetailView.as_view(), name = 'post'),
    path('post/create', views.CreateRecipeView.as_view(), name = 'create_post'),
    path('post/<int:pk>/update', views.UpdateRecipeView.as_view(), name = 'update'),
    path('post/add', views.CreateCategoryView.as_view(), name = 'create_category'),
    
]