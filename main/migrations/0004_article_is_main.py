# Generated by Django 2.2 on 2020-07-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200726_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_main',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
