from django.db import models
import uuid


class Token(models.Model):
    token = models.UUIDField(
        default = uuid.uuid4,
        unique=True
    )
