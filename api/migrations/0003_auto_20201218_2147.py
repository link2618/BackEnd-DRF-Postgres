# Generated by Django 3.1.4 on 2020-12-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201218_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo',
            field=models.CharField(default='CLIENTE', help_text='Tipo de Usuario', max_length=100),
        ),
    ]
