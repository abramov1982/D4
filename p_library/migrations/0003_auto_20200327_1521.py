# Generated by Django 2.2.6 on 2020-03-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200322_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='pub_house',
            field=models.CharField(max_length=128),
        ),
    ]
