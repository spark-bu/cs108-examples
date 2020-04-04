from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.TextField(blank = False)
    def __str__(self):
        return self.name

class Quote(models.Model):
    '''Encapsulate the idea of a quote (i.e text).'''
    text = models.TextField(blank=True)
    #person = models.ForeignKey('Person', on_delete = "CASCADE")
    def __str__(self):
        ''' Return a string Representation of this object.'''
        return '"%s" - %s' % (self.text, self.person.name)

class Image(models.Model):
    image_url = models.URLField(blank=True)
    person = models.ForeignKey('Person', on_delete = "CASCADE")

    def __str__(self):
        ''' Return a string Representation of this object.'''

        return self.image_url
