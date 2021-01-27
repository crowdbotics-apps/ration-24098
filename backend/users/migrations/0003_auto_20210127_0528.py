# Generated by Django 2.2.17 on 2021-01-27 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
        ('users', '0002_auto_20210127_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='background_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='featured_playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_featured_playlist', to='playlist.Playlist'),
        ),
        migrations.AddField(
            model_name='user',
            name='sanctioned',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
