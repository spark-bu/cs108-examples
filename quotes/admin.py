from django.contrib import admin
from .models import Quote, Person, Image
# Register your models here.
admin.site.register(Quote)
admin.site.register(Person)
admin.site.register(Image)