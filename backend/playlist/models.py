from django.conf import settings
from django.db import models


class Playlist(models.Model):
    "Generated Model"
    content_cards = models.ManyToManyField(
        "content.Content",
        related_name="playlist_content_cards",
    )
    last_updated = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    time_created = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        max_length=50,
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )


# Create your models here.
