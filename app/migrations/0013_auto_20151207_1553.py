# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20151207_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskproject',
            name='id_project',
            field=models.ForeignKey(related_name='risk_projects', to='app.Project'),
        ),
    ]
