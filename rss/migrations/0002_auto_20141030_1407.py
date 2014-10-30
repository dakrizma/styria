# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lista',
            options={'verbose_name_plural': 'liste'},
        ),
        migrations.AlterField(
            model_name='lista',
            name='status',
            field=models.CharField(max_length=1, choices=[(True, b'Da'), (False, b'Ne')]),
            preserve_default=True,
        ),
    ]
