# Generated by Django 2.0.1 on 2018-02-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180128_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_developer',
            field=models.BooleanField(default=False),
        ),
    ]