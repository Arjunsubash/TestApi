# Generated by Django 3.0.8 on 2021-05-07 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiTest', '0002_auto_20210507_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowed_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]