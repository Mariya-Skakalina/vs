from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Genre(models.Model):
    name = models.CharField('Название', max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Verse(models.Model):
    title = models.CharField('Название произведения', max_length=300, null=False, blank=False, unique=True)
    verses = RichTextUploadingField('Стих', null=True, blank=True, unique=True)
    genre = models.ForeignKey('Genre', verbose_name="Жанр", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Home(models.Model):
    text = RichTextUploadingField(verbose_name='Текст', null=True, blank=True, unique=True)

    def __str__(self):
        return self.text

class Biography(models.Model):
    text_Biography = RichTextUploadingField(verbose_name='Биография', blank=False, null=False)

    def __str__(self):
        return self.text_Biography