# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_project_id_categroy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='id_categroy',
            new_name='id_category',
        ),
    ]
