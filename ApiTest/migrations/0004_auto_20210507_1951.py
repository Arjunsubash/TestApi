# Generated by Django 3.0.8 on 2021-05-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiTest', '0003_borrowed_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_book',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
