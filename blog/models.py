from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) #character field has maximum length as 100
    content = models.TextField() #unrestricted text
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete = models.CASCADE) #many to one relationship

    def __str__(self):
        return self.title 
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    