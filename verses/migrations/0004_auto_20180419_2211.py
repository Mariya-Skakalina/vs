# Generated by Django 2.0.4 on 2018-04-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verses', '0003_auto_20180419_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verse',
            name='date',
            field=models.DateField(),
        ),
    ]