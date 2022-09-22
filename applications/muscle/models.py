from django.db import models

class Muscle(models.Model):
    name = models.CharField("Músculo", max_length=40, null=False, blank=False)

    class Meta:
        verbose_name = 'Músculo'
        verbose_name_plural = 'Músculos'

    def __str__(self):
        return self.name
