# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.

from django.db import models

class Employeeteam(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Employee team"
        verbose_name_plural = "Employee teams"

    def __unicode__(self):
        return self.name

class Employeename(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employeeteam = models.ForeignKey(Employeeteam)

    class Meta:
        verbose_name = "Employee name"
        verbose_name_plural = "Employee names"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
