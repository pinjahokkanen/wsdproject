# Generated by Django 2.0.1 on 2018-02-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_merge_20180219_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('PUZZLE', 'Puzzle'), ('SPORTS', 'Sports'), ('EDUCATIONAL', 'Educational'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=12),
        ),
    ]
