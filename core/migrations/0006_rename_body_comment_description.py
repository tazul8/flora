# Generated by Django 3.2.9 on 2021-11-29 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211129_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='description',
        ),
    ]
