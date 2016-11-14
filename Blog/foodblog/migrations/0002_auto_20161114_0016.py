# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-13 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(),
        ),
    ]
