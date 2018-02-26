# Generated by Django 2.0.1 on 2018-02-26 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.CharField(max_length=255, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=250)),
                ('url', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.URLField(blank=True)),
                ('pubDate', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('PUZZLE', 'Puzzle'), ('SPORTS', 'Sports'), ('EDUCATIONAL', 'Educational'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, default=0, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('paymentReference', models.IntegerField(default=0, null=True)),
                ('paymentDate', models.DateTimeField(default=None, null=True)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('games', models.ManyToManyField(blank=True, default=None, to='webapp.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('developer', models.BooleanField(default=False)),
                ('games', models.ManyToManyField(related_name='_profile_games_+', to='webapp.Game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.Profile'),
        ),
        migrations.AddField(
            model_name='gamestate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Profile'),
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='developed_games', to='webapp.Profile'),
        ),
    ]
