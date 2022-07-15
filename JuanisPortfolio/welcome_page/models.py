from django.db import models


class NewUsers(models.Model):
    name = models.CharField(max_length=38)
    user_name = models.CharField(max_length=35)


