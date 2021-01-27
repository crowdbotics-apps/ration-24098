from django.conf import settings
from django.db import models


class Playlist(models.Model):
    "Generated Model"
    content_cards = models.ManyToManyField(
        "content.Content",
        related_name="playlist_content_cards",
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=50,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )


# Create your models here.
