# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=1, choices=[(b'd', b'Da'), (b'n', b'Ne')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
