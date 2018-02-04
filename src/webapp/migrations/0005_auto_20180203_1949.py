# Generated by Django 2.0.1 on 2018-02-03 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180203_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='developed_games',
        ),
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='developed_games', to='webapp.Profile'),
        ),
    ]