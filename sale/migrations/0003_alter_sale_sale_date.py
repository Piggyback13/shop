# Generated by Django 4.0.6 on 2022-07-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_sale_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(),
        ),
    ]
