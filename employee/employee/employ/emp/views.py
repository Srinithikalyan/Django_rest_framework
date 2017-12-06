# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from models import Employeeteam, Employeename
from serializers import EmployeeteamSerializer, EmployeenameSerializer

class EmployeenameViewSet(viewsets.ModelViewSet):
    queryset = Employeename.objects.all()
    serializer_class = EmployeenameSerializer

class EmployeeteamViewSet(viewsets.ModelViewSet):
    queryset = Employeeteam.objects.all()
    serializer_class = EmployeeteamSerializer
