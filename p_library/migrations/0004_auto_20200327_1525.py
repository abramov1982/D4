# Generated by Django 2.2.6 on 2020-03-27 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200327_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='pub_house',
            new_name='name',
        ),
    ]
