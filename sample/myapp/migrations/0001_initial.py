# Generated by Django 4.2.6 on 2023-10-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='football_player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=40)),
                ('player_position', models.CharField(max_length=50)),
                ('player_age', models.IntegerField()),
                ('jersy_no', models.IntegerField()),
                ('player_native', models.CharField(max_length=40)),
            ],
        ),
    ]
