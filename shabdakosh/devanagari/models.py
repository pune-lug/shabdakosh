from django.db import models


class shabda(models.Model):
    shabda = models.CharField(max_length=200, unique=True)
    kiti_vela = models.PositiveIntegerField()

    def __str__(self):
        return self.shabda
