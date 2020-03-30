from django.db import models

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the idea of a quote (i.e text).'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.EmailField(blank=True)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        ''' Return a string Representation of this object.'''
        return '"%s" - %s' % (self.first_name, self.last_name)