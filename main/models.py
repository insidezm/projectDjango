from django.db import models


class TextAn(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
