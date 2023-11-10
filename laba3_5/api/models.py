from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(blank=True, default=False)
