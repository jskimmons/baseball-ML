# Generated by Django 2.0.7 on 2018-08-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0004_todaygame_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='todaygame',
            name='date',
            field=models.CharField(default='def', max_length=200),
            preserve_default=False,
        ),
    ]
