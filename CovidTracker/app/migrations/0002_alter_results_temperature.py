# Generated by Django 3.2.12 on 2022-02-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='temperature',
            field=models.FloatField(null=True),
        ),
    ]