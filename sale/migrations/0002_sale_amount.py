# Generated by Django 4.0.6 on 2022-07-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
