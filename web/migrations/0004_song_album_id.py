# Generated by Django 3.0.6 on 2020-05-31 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200531_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album_id',
            field=models.IntegerField(null=True),
        ),
    ]
