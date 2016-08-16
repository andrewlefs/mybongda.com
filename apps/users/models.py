from django.db import models
from django.conf import settings


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile', primary_key=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
        db_table = 'user_profile'
