from django.db.models import Avg
from rest_framework import serializers

from .models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        average_rate =  obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if average_rate:
            return round(average_rate, 1)
        
        return None
        
    def validate_synopsis(self, value):
        
        if len(value) > 200:
            raise serializers.ValidationError("A sinopse não pode ser maior que 200 caracteres.")
        return value
