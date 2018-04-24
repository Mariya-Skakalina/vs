# Generated by Django 2.0.4 on 2018-04-19 19:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verses', '0004_auto_20180419_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='date',
        ),
        migrations.RemoveField(
            model_name='verse',
            name='verse',
        ),
        migrations.AddField(
            model_name='verse',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='verses.Genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='verse',
            name='verses',
            field=ckeditor.fields.RichTextField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
    ]