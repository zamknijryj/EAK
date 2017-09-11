from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    STOPNIE = (
        ('szeregowy', 'szer'),
        ('starsz szeregowy', 'st.szer'),
        ('major', 'mjr')
    )

    user = models.ForeignKey(User, related_name='user_profile')
    podpis = models.CharField(max_length=140)
    stopien = models.CharField(max_length=15, choices=STOPNIE, default='major')

    class Meta:
        ordering = ['user', ]

    def __str__(self):
        return "Profil użytkownika {}".format(self.user)
