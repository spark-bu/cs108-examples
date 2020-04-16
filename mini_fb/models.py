from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the idea of a quote (i.e text).'''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.EmailField(blank=True)
    profile_image_url = models.URLField(blank=True)
    friends = models.ManyToManyField("self")


    def __str__(self):
        ''' Return a string Representation of this object.'''
        return '"%s" - %s' % (self.first_name, self.last_name)

    def get_status_message(self):
        status = StatusMessage.objects.filter(profile=self.pk)
        return status
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    def get_friends(self):
        queryset = self.friends.all().exclude(pk=self.pk)
        return queryset
    def get_news_feed(self):
        news = StatusMessage.objects.all().order_by("-timestamp")
        return news


class StatusMessage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank = True)
    profile = models.ForeignKey('Profile', on_delete="CASCADE")
    image = models.ImageField(blank =True)

    def __str__(self):
        ''' Return a string Representation of this object.'''
        return '%s  %s' % (self.timestamp, self.message)