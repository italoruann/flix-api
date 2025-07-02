from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
    
    def validate_comment(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Os comentários não podem ser maiores que 500 caracteres.")
        return value