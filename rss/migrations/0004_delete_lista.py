# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0003_delete_lista'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lista',
        ),
    ]
