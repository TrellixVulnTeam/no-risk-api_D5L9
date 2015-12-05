# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_project_risks'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('username', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='id_owner',
            field=models.ForeignKey(related_name='owner', to='app.UserCustom'),
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to='app.UserCustom', related_name='members'),
        ),
    ]
