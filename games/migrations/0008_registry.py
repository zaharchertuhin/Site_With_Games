# Generated by Django 3.2.3 on 2021-06-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_game_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
