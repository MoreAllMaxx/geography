from django.db import models


class Note(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Тема')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание')
