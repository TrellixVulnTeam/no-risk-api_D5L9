# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151207_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id_categroy',
        ),
    ]
