# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mathfield.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MathfieldTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latex', mathfield.models.MathField()),
            ],
        ),
    ]
