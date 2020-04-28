'''
Author: Soo Whan Park
Email: spark96@bu.edu
Filename: apps.py
Description: Initate the new application, and register it on the settings.py
'''
from django.apps import AppConfig

#Initiate the new app called foodie
class FoodieConfig(AppConfig):
    name = 'foodie'
