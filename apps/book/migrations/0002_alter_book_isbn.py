# Generated by Django 5.0 on 2023-12-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(db_index=True, max_length=18, unique=True, verbose_name='International Standard Book Number'),
        ),
    ]
