from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView, CreateProfileView, UpdateProfileView,create_status_message,DeleteStatusMessageView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name = 'home'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name = 'profile'),
    path('create_profile', CreateProfileView.as_view(), name = 'create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name = 'update'),
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>', DeleteStatusMessageView.as_view(), name = 'delete_status'),
    path('profile/<int:pk>/post_status', create_status_message, name = 'post_status'),

]