# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 07:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='FormSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('schema', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.AddField(
            model_name='formresponse',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.FormSchema'),
        ),
    ]