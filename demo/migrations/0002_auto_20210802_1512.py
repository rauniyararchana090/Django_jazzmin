# Generated by Django 3.1.2 on 2021-08-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Author'),
        ),
    ]
