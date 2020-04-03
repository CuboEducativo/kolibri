# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-26 19:25
from __future__ import unicode_literals

from django.db import migrations
from django.db import models

from ..constants.facility_presets import choices as facility_choices

# This is necessary because:
# 1. The list generator has an unpredictable order, and when items swap places
#    then this would be picked up as a change in Django if we had used
# 2. These choices can be changed in facility_configuration_presets.json
#    and such change should not warrant warnings that models are inconsistent
#    as it has no impact.
# Notice: The 'choices' property of a field does NOT have any impact on DB
# See: https://github.com/learningequality/kolibri/pull/3180


class Migration(migrations.Migration):

    dependencies = [("kolibriauth", "0006_auto_20171206_1207")]

    operations = [
        migrations.AlterField(
            model_name="facilitydataset",
            name="preset",
            field=models.CharField(
                choices=facility_choices, default="nonformal", max_length=50
            ),
        ),
        migrations.AlterUniqueTogether(name="facilityuser", unique_together=set([])),
    ]