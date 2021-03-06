# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import s3upload.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_filename', s3upload.fields.S3UploadField(blank=True, dest='custom_filename')),
            ],
        ),
        migrations.CreateModel(
            name='Kitten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', s3upload.fields.S3UploadField(blank=True, dest='videos')),
                ('image', s3upload.fields.S3UploadField(blank=True, dest='images')),
                ('pdf', s3upload.fields.S3UploadField(blank=True, dest='pdfs')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat.Cat')),
            ],
        ),
    ]
