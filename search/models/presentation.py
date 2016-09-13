# coding=utf-8
"""Presentation model"""
from django.db import models


class Presentation(models.Model):
    custom_id = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=250)
    creator_name = models.CharField(max_length=250)
    creator_profile_url = models.CharField(max_length=250)

    date_added = models.DateTimeField(db_index=True, auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        """This defines a format, to display a record in django admin"""
        return '{} ({})'.format(
            self.custom_id, self.creator_name
        )
