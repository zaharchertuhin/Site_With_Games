# Generated by Django 3.2.3 on 2021-05-31 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='slug',
        ),
    ]