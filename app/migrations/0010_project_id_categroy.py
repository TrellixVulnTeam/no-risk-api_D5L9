# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_project_id_categroy'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='id_categroy',
            field=models.ForeignKey(default='2', to='app.Category'),
        ),
    ]
