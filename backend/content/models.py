from django.conf import settings
from django.db import models


class Content(models.Model):
    "Generated Model"
    url = models.URLField()
    image_url = models.URLField()
    title = models.CharField(
        max_length=512,
    )
    commentary = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="content_owner",
    )


# Create your models here.
