# Generated by Django 4.0.4 on 2022-09-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableUsabilityOperators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_name', models.CharField(default=' ', max_length=50)),
                ('_from', models.IntegerField(default=1)),
                ('_into', models.IntegerField(default=1)),
                ('_join', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
