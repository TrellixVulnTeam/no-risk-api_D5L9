# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('id_categroy', models.TextField()),
                ('description', models.TextField()),
                ('start_date', models.TextField()),
                ('end_date', models.TextField()),
                ('id_owner', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('category', models.TextField()),
                ('description', models.TextField()),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Risk_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('id_project', models.TextField()),
                ('id_risk', models.TextField()),
                ('probability', models.TextField()),
                ('impact', models.TextField()),
                ('factors', models.TextField()),
                ('reduction', models.TextField()),
                ('supervision', models.TextField()),
            ],
        ),
    ]
