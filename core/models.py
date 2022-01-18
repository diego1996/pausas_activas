from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Company(models.Model):
    owner = models.OneToOneField(User, verbose_name='Usuario dueño', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nombre de la empresa', max_length=100)
    logo = models.ImageField(verbose_name='Logo de la empresa', upload_to='company/logos/')
    mascot = models.FileField(verbose_name='Mascota de la empresa', upload_to='company/mascots/')
    primary_color = ColorField(verbose_name='Color primario de la empresa', default='#4a5bb2')
    secondary_color = ColorField(verbose_name='Color secundario de la empresa', default='#a48421')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.name}'


class ActivePause(models.Model):
    company = models.ForeignKey(Company, verbose_name='Empresa', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nombre de la pausa activa', max_length=100)
    slug = models.SlugField(db_index=True, verbose_name='Ruta Web', max_length=150)
    description = models.TextField(verbose_name='Descripción', max_length=100, blank=True, null=True)
    image = models.ImageField(verbose_name='Imágen', upload_to='active-pauses/images/', blank=True, null=True)
    icon_svg = models.FileField(verbose_name='Icono en SVG', upload_to='active-pauses/icons/', blank=True, null=True)
    number_of_exercises = models.IntegerField(verbose_name='Número de ejercicios', default=0)
    duration = models.CharField(verbose_name='Duración', max_length=10)

    class Meta:
        verbose_name = 'Pausa Activa'
        verbose_name_plural = 'Pausas Activas'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ActivePause, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Activity(models.Model):
    active_pause = models.ForeignKey(ActivePause, verbose_name='Pausa activa', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nombre de la actividad', max_length=100)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return f'{self.name}'


class Prevent(models.Model):
    active_pause = models.ForeignKey(ActivePause, verbose_name='Pausa activa', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nombre de la prevención', max_length=100)

    class Meta:
        verbose_name = 'Que previene'
        verbose_name_plural = 'Que previene'

    def __str__(self):
        return f'{self.name}'


class Video(models.Model):
    active_pause = models.ForeignKey(ActivePause, verbose_name='Pausa activa', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nombre del video', max_length=100)
    image = models.ImageField(verbose_name='Imágen', upload_to='active-pauses/videos/images/', blank=True, null=True)
    video = models.FileField(verbose_name='Video', upload_to='active-pauses/videos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return f'{self.name}'
