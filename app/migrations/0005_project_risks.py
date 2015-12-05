# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151202_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='risks',
            field=models.ManyToManyField(to='app.Risk', through='app.RiskProject'),
        ),
    ]
