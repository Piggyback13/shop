# Generated by Django 4.0.6 on 2022-07-19 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_alter_sale_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
