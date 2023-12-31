# Generated by Django 5.0 on 2023-12-12 10:49

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('title', models.CharField(db_index=True, max_length=500, verbose_name='Book Title')),
                ('isbn', models.CharField(db_index=True, max_length=13, unique=True, verbose_name='International Standard Book Number')),
                ('publication_year', models.PositiveSmallIntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2023)], verbose_name='Publication Year')),
                ('brief_summary', models.TextField(verbose_name='Brief Summary')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='BookAuthor', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
