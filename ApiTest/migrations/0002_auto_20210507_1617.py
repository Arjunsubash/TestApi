# Generated by Django 3.0.8 on 2021-05-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiTest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bount',
        ),
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]