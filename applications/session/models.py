from django.db import models
from django.utils.timezone import now

from applications.machine.models import Machine


# Create your models here.


class Session(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    uploading_time = models.DateTimeField("Fecha de carga", default=now)

    class Meta:
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'

    def __str__(self):
        return str(self.machine) + " - " + str(self.uploading_time)

class Series(models.Model):
    reps = models.PositiveIntegerField("Repeticiones", blank=False, null=False)
    intensity = models.PositiveIntegerField("Intesidad/Peso")
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'

    def __str__(self):
        return str(self.session) + " - " + str(self.reps)


class TimeSession(Session):
    time = models.DurationField("Tiempo", blank=False, null=False)
    spending = models.FloatField("Gasto/Calorías", default=0)

    class Meta:
        verbose_name = 'Sesión de tiempo'
        verbose_name_plural = 'Sesiones de tiempo'

    def __str__(self):
        return str(self.machine) + " - " + str(self.time)