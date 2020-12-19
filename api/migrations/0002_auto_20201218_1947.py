# Generated by Django 3.1.4 on 2020-12-19 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipo',
            field=models.CharField(blank=True, default='CLIENTE', help_text='Tipo de Usuario', max_length=100),
        ),
    ]
