# Generated by Django 3.2.16 on 2023-05-17 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_video_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.CharField(default=12345, max_length=50),
            preserve_default=False,
        ),
    ]
