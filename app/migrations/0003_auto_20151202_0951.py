# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151202_0944'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Risk_Project',
            new_name='RiskProject',
        ),
    ]
