# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets

from libros import serializers

from libros import models

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class LibrosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.LibroSerializer
    queryset = models.libros.objects.all()
