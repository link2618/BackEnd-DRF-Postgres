# Generated by Django 3.1.4 on 2020-12-25 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='user_id',
            new_name='user',
        ),
    ]
