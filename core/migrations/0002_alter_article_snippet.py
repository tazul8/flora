# Generated by Django 3.2.9 on 2021-11-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.TextField(),
        ),
    ]
