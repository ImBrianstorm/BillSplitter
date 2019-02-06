"""User's models"""

from django.db import models
from django.contrib.auth.models import User

class Splitter(models.Model):
    """Extends user information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media/users/pictures', blank=True, null=True)
    active_bill = models.BooleanField('Splitter activo', blank=True, default=False)

    def __str__(self):
        return '@' + self.user.username

    def is_active(self):
        return self.active_bill