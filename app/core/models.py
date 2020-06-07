from django.db import models
import uuid
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    creation_date = models.DateField('Creation date', auto_now_add=True)
    modified_date = models.DateField('Modified date', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket')
    )

    service = models.CharField('Service', max_length=100)
    description = models.TextField('Description', max_length=200)
    icon = models.CharField('Icon', max_length=25, choices=ICON_CHOICES)

    def __str__(self):
        return self.service


class Occupation(Base):
    occupation = models.CharField('Cargo', max_length=100)

    def __str__(self):
        return self.occupation


class Employee(Base):
    name = models.CharField('Name', max_length=100)
    occupation = models.ForeignKey('core.Occupation', verbose_name='Occupation', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=255)
    photo = StdImageField('Photo', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    def __str__(self):
        return self.name
