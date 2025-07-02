from rest_framework import serializers

from .models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
    
    def get_rate(self, obj):
        return 5
        
    def validate_synopsis(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("A sinopse não pode ser maior que 200 caracteres.")
        return value
