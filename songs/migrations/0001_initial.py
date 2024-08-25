# Generated by Django 4.2.15 on 2024-08-25 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('danceability', models.FloatField()),
                ('energy', models.FloatField()),
                ('key', models.IntegerField()),
                ('loudness', models.FloatField()),
                ('mode', models.IntegerField()),
                ('acousticness', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('liveness', models.FloatField()),
                ('valence', models.FloatField()),
                ('tempo', models.FloatField()),
                ('duration_ms', models.BigIntegerField()),
                ('time_signature', models.IntegerField()),
                ('num_bars', models.IntegerField()),
                ('num_sections', models.IntegerField()),
                ('num_segments', models.IntegerField()),
                ('song_class', models.IntegerField(max_length=50)),
            ],
        ),
    ]
