from django.db import models
from applications.muscle.models import Muscle


# Create your models here.

class MachineBrand(models.Model):
    name = models.CharField("Marca", max_length=40, null=False, blank=False)

    class Meta:
        verbose_name = 'Marca de máquina'
        verbose_name_plural = 'Marcas de máquinas'

    def __str__(self):
        return self.name


class Machine(models.Model):
    MACHINE_TYPE_OPTIONS = (
        (0, 'REPS'),
        (1, 'TIME'),
    )

    name = models.CharField("Nombre de la máquina", max_length=40, null=False, blank=False)
    type = models.IntegerField("REPS/TIEMPO", choices=MACHINE_TYPE_OPTIONS, default=0)
    muscle = models.ManyToManyField("muscle.Muscle", blank=True, null=True)
    brand = models.ForeignKey(MachineBrand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Máquina'
        verbose_name_plural = 'Máquinas'

    def __str__(self):
        return str(self.brand) + " - " + self.name
