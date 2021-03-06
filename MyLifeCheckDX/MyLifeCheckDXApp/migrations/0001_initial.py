# Generated by Django 3.1.1 on 2021-05-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BBCNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('title', models.CharField(max_length=512)),
                ('url', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='NikkeiNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('title', models.CharField(max_length=512)),
                ('url', models.CharField(max_length=512)),
            ],
        ),
    ]
