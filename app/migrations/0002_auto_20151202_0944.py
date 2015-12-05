# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='id_categroy',
            field=models.ForeignKey(to='app.Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='risk_project',
            name='id_project',
            field=models.ForeignKey(to='app.Project'),
        ),
        migrations.AlterField(
            model_name='risk_project',
            name='id_risk',
            field=models.ForeignKey(to='app.Risk'),
        ),
        migrations.AddField(
            model_name='member',
            name='id_project',
            field=models.ForeignKey(to='app.Project'),
        ),
        migrations.AddField(
            model_name='member',
            name='id_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
