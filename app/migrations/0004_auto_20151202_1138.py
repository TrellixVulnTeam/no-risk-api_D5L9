# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20151202_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id_project',
        ),
        migrations.RemoveField(
            model_name='member',
            name='id_user',
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='members'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owner'),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
