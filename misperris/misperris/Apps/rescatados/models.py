from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


# Create your models here.

ESTADOS= (
    ('Rescatado', 'Rescatado'),
    ('Disponible', 'Disponible'),
    ('Adoptado', 'Adoptado'),
)

class Rescate (models.Model):
    fotografia_perro = models.ImageField
    nombre_perro = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=20)
    estado = models.CharField(max_length=30, choices=ESTADOS, null=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre_perro

    class Meta:
        permission = (
            ('adoptantes', _('Adoptantes')),
        )