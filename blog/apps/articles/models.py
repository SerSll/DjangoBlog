# coding:utf-8
from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime


class Article(models.Model):

    title = models.CharField('Название статьи', max_length=200)    # поле для ввода небольшого текста
    text = models.TextField('Содержание статьи')  # Поле для ввода большого текста
    date_publ = models.DateTimeField('Дата публикации')   # Дата публикации

    def __str__(self):
        return self.title

    def last_7_days(self):
        return self.date_publ >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'   # Руссифицируем админку


class Comment(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Привязка к статье
    name_publ = models.CharField('Имя автора комм.', max_length=60)
    text = models.CharField('Содержание комментария', max_length=200)

    def __str__(self):
        return self.name_publ

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'  # Руссифицируем админку


