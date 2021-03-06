# -*- coding: utf-8 -*-
# Copyright 2017-2018 Dunbar Security Solutions, Inc.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.10.1 on 2017-03-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pipes', '0001_initial'),
        ('datasieves', '0001_initial'),
        ('datachutes', '0001_initial'),
        ('datamungers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datachute',
            name='endpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pipes.Pipe'),
        ),
        migrations.AddField(
            model_name='datachute',
            name='munger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamungers.DataMunger'),
        ),
        migrations.AddField(
            model_name='datachute',
            name='sieve',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chutes', related_query_name='chute', to='datasieves.DataSieve'),
        ),
        migrations.AlterUniqueTogether(
            name='datachute',
            unique_together=set([('sieve', 'munger')]),
        ),
    ]
