# Generated by Django 3.0.6 on 2020-06-02 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_song_album_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Album'),
        ),
    ]
