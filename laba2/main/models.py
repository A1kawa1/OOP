from django.db import models


class Dictionary(models.Model):
    word = models.CharField(verbose_name='слово', max_length=50)
    translation = models.CharField(verbose_name='перевод', max_length=50)

    class Meta:
        unique_together = (('word', 'translation'),)
