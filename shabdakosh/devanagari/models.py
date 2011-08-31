from django.db import models
from django.contrib import admin

# Create your models here.

class shabda(models.Model):
    shabda = models.CharField(max_length=200, unique=True)
    kiti_vela = models.PositiveIntegerField()
    def __unicode__(self):
        return '%s' % self.shabda
