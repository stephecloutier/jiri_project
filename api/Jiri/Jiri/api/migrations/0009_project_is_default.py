# Generated by Django 2.0 on 2018-01-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180118_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
