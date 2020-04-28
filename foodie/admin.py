'''
Author: Soo Whan Park
Email: spark96@bu.edu
Filename: admin.py
Description: Register the Models in the localAddress/admin/
'''

from django.contrib import admin
from foodie.models import Type, Recipe

#Register the models in the admin
admin.site.register(Type)
admin.site.register(Recipe)

# Register your models here.
