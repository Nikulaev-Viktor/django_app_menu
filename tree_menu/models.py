from django.db import models
from django.urls import reverse, NoReverseMatch

NULLABLE = {'blank': True, 'null': True}


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', **NULLABLE, on_delete=models.CASCADE, related_name='children')
    named_url = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            return reverse(self.named_url)
        except NoReverseMatch:
            return self.url

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
