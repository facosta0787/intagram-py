from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    """ Foreign Keys """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    """ Table Fields """
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)
