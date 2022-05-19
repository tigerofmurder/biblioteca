# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets

from libros import serializers

from libros import models

from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination


# Create your views here.

class PagintedSet(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class LibrosViewSet(viewsets.ModelViewSet):
    pagination_class = PagintedSet
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.LibroSerializer
    queryset = models.libros.objects.all()
    
