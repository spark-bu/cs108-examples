from django.urls import path
from .views import ShowAllProfilesView, ShowProfilePageView

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name = 'home'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name = 'profile')
]