from django.db import models

class Date_info(models.Model):
    date = models.CharField(max_length=10)
