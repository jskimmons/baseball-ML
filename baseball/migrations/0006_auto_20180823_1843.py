# Generated by Django 2.0.7 on 2018-08-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0005_todaygame_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todaygame',
            name='date',
        ),
        migrations.AlterField(
            model_name='todaygame',
            name='prediction',
            field=models.CharField(max_length=10),
        ),
    ]
