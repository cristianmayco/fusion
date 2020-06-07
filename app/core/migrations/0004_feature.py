# Generated by Django 3.0.7 on 2020-06-07 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200607_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified date')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=255, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-cog', 'Gear'), ('lni-leaf', 'Leaf'), ('lni-laptop-phone', 'Mobile'), ('lni-rocket', 'Rocket')], max_length=25, verbose_name='Icon')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]