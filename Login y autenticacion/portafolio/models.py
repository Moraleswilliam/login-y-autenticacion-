from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    descripcion= CharField(max_length=250)
    image = models.ImageField(upload_to="portafolio/imagenes", default='path_to_default_image.jpg')
    url= URLField(blank=True)
    date= DateField(default=date.today)
    
    def __str__(self) -> str:
        return self.title