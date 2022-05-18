from rest_framework import serializers
from libros import models


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.libros
        fields = '__all__' 